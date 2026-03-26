# AI-Product-Discovery-Optimiser

## Goal
Test whether a product page can become more discoverable in AI-generated shopping recommendations by improving content structure, FAQ coverage, comparison content, and schema markup.

## Product
28cm Non-Stick Frying Pan

## Why this project matters
Consumers are increasingly using AI tools such as ChatGPT and Perplexity to ask what products to buy. This project tests whether improving the structure and wording of a product page makes the product easier for AI systems to understand and recommend.

## Method
1. Create a weak baseline product page.
2. Create an improved version with conversational copy, FAQs, comparison content, and structured data.
3. Use the same fixed prompts to evaluate both versions.
4. Record visibility and recommendation quality.
5. Compare baseline vs optimised results.

## Files
- `pages/baseline_product_page.md`
- `pages/optimised_product_page.md`
- `schema.json`
- `data/prompts.txt`
- `data/results_baseline.csv`
- `data/results_after.csv`

## Metrics
- Visibility rate
- Average position when mentioned
- Query match rate
- Recommendation quality score

## Status
Project setup complete. Testing in progress.