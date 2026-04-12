# Verification Scenarios

Eight frozen dry-run test cases for the skills library. Each scenario:
1. Describes a situation (screenshot description + context).
2. Lists the expected skill-invocation path.
3. States the expected final action (`X`, `Y`, or `Z`) with justification.

Scenarios are used to validate that the skill set routes correctly. Run a fresh Claude session with only this library available against each scenario and compare outputs to the expected-answer key in each file.

## Scenario index

1. `scenario-01-bullish-breakout-on-tradingview.md` — AAPL 1H breakout with volume. Expected: X (with full order spec).
2. `scenario-02-earnings-gap-down.md` — Held name gaps down 15% on earnings miss. Expected: Y (STOP_OUT / THESIS_BREAK).
3. `scenario-03-fomc-in-5-minutes.md` — Setup present but FOMC release imminent. Expected: Z (news blackout).
4. `scenario-04-unexpected-popup-on-screen.md` — Order ticket overlayed by 2FA prompt. Expected: Z (screen ambiguity → safety-kill-switch).
5. `scenario-05-buffett-candidate-screen.md` — KO quality screen candidate at fair price. Expected: Z (no margin of safety, wait).
6. `scenario-06-position-sizing-2pct-account-risk.md` — Operator requests 2% risk on a trade. Expected: Z (cap violation) + explain.
7. `scenario-07-crypto-perp-funding-negative.md` — BTC perp with funding at extreme. Expected: Z (context only, no setup).
8. `scenario-08-drawdown-limit-hit.md` — Daily loss at 3%. Expected: Z (hard kill → flatten all → session lock).

## How to run

For each scenario:
1. Feed the scenario content to a fresh Claude session.
2. Give the session access only to `.claude/skills/`.
3. Ask: "Which skills do you load, in what order, and what is your final X/Y/Z output?"
4. Compare to the expected-answer section at the bottom of each scenario file.

Any mismatch is a defect in either the scenario or the skill set — both should be reviewed.
