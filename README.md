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

## Results

The optimised product page improved recommendation performance in controlled LLM evaluations.

- Query match rate increased from 60% to 80% (+20 percentage points).
- Average recommendation score increased from 2.6 to 4.0 (+1.4 points).
- Relative recommendation-score improvement: 53.8%.
- Visibility rate remained 100% in both phases because the product was always included in the evaluation context, so visibility was not the main performance signal in this controlled experiment.

## Key Insight

The biggest gains came from adding conversational copy, beginner-focused wording, FAQ content, comparison language, and clearer product attributes. The only weak area that remained was induction-related queries, because the page still did not explicitly confirm induction compatibility.


## Claim

Improved LLM query-match rate from 60% to 80% and average recommendation score from 2.6 to 4.0 by optimising product content for conversational AI discovery.