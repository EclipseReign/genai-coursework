"""Measure retrieval coverage and verify cited answers on fixed handbook queries."""

import argparse
import json
import re
from pathlib import Path

from rag import ROOT, ask


def evaluate(case):
    reply = ask(case["question"])
    expected = set(case["sources"])
    retrieved = {match["id"] for match in reply["retrieved"]}
    citations = set(reply["citations"])
    if expected:
        correct = (
            reply["status"] == "answered"
            and citations == expected
            and all(re.search(fact, reply["answer"], re.IGNORECASE) for fact in case["facts"])
        )
    else:
        correct = reply["status"] == "unanswered" and not citations
    return {
        "case": case["case"], "question": case["question"],
        "expected_sources": case["sources"],
        "all_expected_sources_retrieved": expected <= retrieved if expected else None,
        "passed": correct, **reply,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, help="write detailed results as JSON")
    args = parser.parse_args()
    cases = json.loads((ROOT / "evaluation" / "cases.json").read_text(encoding="utf-8"))
    results = []
    for case in cases:
        result = evaluate(case)
        results.append(result)
        label = "PASS" if result["passed"] else "FAIL"
        print(f"{label:4} {result['case']:18} {result['metrics']['total_ms']:6} ms", flush=True)
    answerable = [result for result in results if result["expected_sources"]]
    summary = {
        "scenario_passes": sum(result["passed"] for result in results),
        "scenarios": len(results),
        "all_gold_sources_in_top_4": sum(result["all_expected_sources_retrieved"] for result in answerable),
        "answerable_scenarios": len(answerable),
    }
    print(json.dumps(summary, indent=2))
    if args.report:
        args.report.write_text(
            json.dumps({"summary": summary, "results": results}, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    return 0 if summary["scenario_passes"] == summary["scenarios"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
