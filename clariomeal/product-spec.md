# ClarioMeal Product Spec

## Positioning

ClarioMeal is an AI nutrition confidence coach. It helps users log meals quickly while showing how much to trust each estimate and what one correction would improve it most.

## Name Direction

Working name: `ClarioMeal`

Rationale: `Clario` suggests clarity and honesty, which supports the confidence-first product angle. A trademark and App Store naming check is still required before launch.

## Core Experience

1. User answers a short goal onboarding.
2. User snaps or uploads a meal photo.
3. Server analyzes image with OpenAI vision through a PHP API proxy.
4. App shows calories, macros, ingredient cards, confidence, and hidden-calorie flags.
5. User confirms or edits with quick correction chips.
6. Weekly check-in adapts calorie/macro targets from trend weight and adherence.

## MVP Scope

- SwiftUI iOS app.
- English default.
- 13 extra languages: Turkish, Spanish, French, German, Italian, Portuguese, Dutch, Arabic, Hindi, Japanese, Korean, Russian, Simplified Chinese.
- Photo picker-based meal scan.
- Mock mode for UI previews and offline development.
- PHP API endpoint: `POST /analyze-meal`.
- Structured JSON response from OpenAI.
- Safe, non-medical wording.
- Animated onboarding and StoreKit 2 paywall.

## Monetization

- Product group: `ClarioMeal Pro`.
- Weekly product id: `com.asilarslan.ClarioMeal.pro.weekly`.
- Yearly product id: `com.asilarslan.ClarioMeal.pro.yearly`.
- Weekly plan includes a 3-day free trial in `ios/ClarioMeal/Configuration/ClarioMeal.storekit`.

## Differentiators

- Confidence range instead of false precision.
- Hidden-calorie detective layer.
- One-question correction flow.
- Clear privacy copy.
- Premium UI that feels calm, exact, and fast.

## Later Roadmap

- Barcode scanner and nutrition label OCR.
- HealthKit and Apple Watch integration.
- Weight trend and adaptive target engine.
- Recipe importer and grocery planning.
- Subscription gate with limited free AI scans.
- Account sync and export.
