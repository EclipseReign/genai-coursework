# Pilot Acceptance Criteria

| Use Case                          | Measurable Outcome                                                                 | Quality/Safety Check (Proposal)                                                | Measurement Method                                                                                  |
|----------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| 1. Software development and testing | Median time from task assignment to approved pull request is reduced compared to baseline | Human-in-the-loop review ensures patches do not introduce security or boundary case bugs | Compare median time and post-merge defect rate on matched tasks; review patch quality and test coverage |
| 2. Enterprise knowledge search    | Average time to verified answer is reduced; high proportion of answers supported by current policy | Access control filters documents correctly; grounding links to accurate, unexpired policy passages | Measure time to verified answer; audit sample answers for correct grounding and access compliance   |
| 3. Customer support with order lookup | Faster resolution of routine inquiries; higher confirmed resolution rate; reduced repeat contacts | Guardrails block unauthorized data disclosure; tool calls validate arguments and enforce permissions | Track resolution time and repeat contacts; test guardrail effectiveness with simulated unauthorized requests |
| 4. Marketing image production     | Reduced time to approved asset; higher approval rate; fewer editing hours per published asset | Human-in-the-loop designer review ensures brand fit, factual accuracy, and usage rights compliance | Compare time and approval metrics; review sample assets for brand and rights compliance             |

Each check is a proposal to ensure safety and quality while measuring practical business value on comparable inputs. See [research-report.md](research-report.md) for detailed context and examples.

---

Ready to publish: true
