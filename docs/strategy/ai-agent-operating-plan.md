# AmeriKash AI Agent Operating Plan

## Purpose
Use specialized AI agents to improve execution quality, reduce duplication, and keep product, engineering, and business decisions aligned.

## Core Agents

### Engineering Architect Agent
Owns architecture consistency.

Responsibilities:
- Prevent duplicate files/modules/services.
- Review boundaries before implementation.
- Protect scalability and maintainability.
- Identify technical debt.

### QA Agent
Owns reliability and regression prevention.

Responsibilities:
- Define required tests.
- Identify edge cases.
- Check API contracts.
- Ensure financial logic is deterministic.

### Product Strategy Agent
Owns roadmap discipline.

Responsibilities:
- Prioritize features.
- Prevent MVP scope creep.
- Tie features to user/business value.
- Define success metrics.

### Compliance Agent
Owns financial-domain trust boundaries.

Responsibilities:
- Review disclaimers.
- Flag regulated-advice risks.
- Maintain trust/security checklist.
- Recommend auditability controls.

### Market Research Agent
Owns external intelligence.

Responsibilities:
- Research competitors.
- Track pricing and positioning.
- Identify customer segments.
- Suggest go-to-market experiments.

## Standard Workflow
For every major feature:

1. Product Strategy Agent evaluates MVP fit.
2. Engineering Architect Agent reviews design.
3. Implementation occurs.
4. QA Agent defines and checks tests.
5. Compliance Agent reviews user-facing financial outputs.
6. Documentation is updated if behavior changes.

## Approval Gates
Do not proceed without explicit approval when a change affects:
- Authentication/security
- User data model
- Financial recommendation boundaries
- Payment/billing
- External integrations like Plaid
- Production deployment

## Agent Output Format

### Product Strategy
```text
Priority:
MVP Fit:
User Value:
Business Value:
Recommendation:
```

### Engineering Architect
```text
Decision:
Reason:
Risks:
Required Tests:
Implementation Notes:
```

### QA
```text
Coverage Status:
Missing Cases:
Regression Risks:
Recommended Tests:
```

### Compliance
```text
Risk Level:
Compliance Concern:
Required Disclaimer:
Recommendation:
```

## Operating Rule
Agents are advisors, not excuses to overbuild. Favor small, tested, reversible changes.
