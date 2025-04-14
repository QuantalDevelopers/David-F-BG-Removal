prompts = {
    "text_prompt": """
        You are analyzing a wine label image. Your task is twofold:

        1. **Extract all readable text from this wine label exactly as it appears.**

        ### Text Extraction Rules:
        - Preserve capitalization, spacing, and formatting exactly as seen.
        - Do not infer, translate, or guess missing text—only extract what is clearly visible.
        - If text is partially cut off, return it as-is without completion.
        - For stylized or cursive fonts, extract characters as best as possible—even approximated characters are better than skipping.
        - Do not merge or "correct" fragmented words.
        - Maintain the vertical and visual order of lines on the label.
        - Ignore decorative, non-informative elements (swirls, flourishes, etc.).
        - Return only raw extracted text in plain format.

        ---

        2. **Structure the extracted text in the following format:**
        Vintage:  
        Producer Name:  
        Fanciful Name / Vineyard Name (if present):  
        Appellation:  
        Grape Variety (if can be inferred):  
        Size (if present, e.g., in ML):  
        Additional Designations (Grand Cru, 1er Cru, Vieilles Vignes, etc.):

        ### Structuring Rules:
        - Do not fabricate, infer, or complete missing details.
        - Categorize only what is clearly visible on the label.
        - Do not assume or invent any values under any circumstance.
        - If a field cannot be confidently filled based solely on the visible text, leave it blank.
        - Only infer a field (e.g., Grape or Appellation) when logically certain and universally standardized (e.g., Châteauneuf-du-Pape = GSM blend).
        - No extra explanation—return only the structured data.
    """,

    "format_prompt": """
    Format the following wine data using this exact structure:

    **Vintage Producer Name (Additional Designations) Appellation Classification Vineyard Name**

    ### Formatting Rules:
    - Output a single clean line. Do not use commas, parentheses, or special characters.
    - Do not include field labels.
    - Avoid ownership names like "Famille J-M Cazes" unless it's the actual estate name.
    - Always prefer wine name over ownership label.
    - Use proper capitalization (e.g., "DOMAINE LEFLAIVE" → "Domaine Leflaive").
    - Use "1er Cru" instead of "Premier Cru" for Burgundy.
    - If "Vieilles Vignes" or other designations are present, place them in double quotes directly after the producer name.
    - Place Premier Cru vineyard name after the phrase "1er Cru".
    - Remove all commas and special characters (including hyphens in appellations like Morey-Saint-Denis → Morey Saint Denis).
    - **Remove all accents or diacritical marks from letters (e.g., "é" becomes "e").**
    - Champagne: Include dosage and style (e.g., Extra Brut Blanc de Noirs) before “Champagne”.
    - New World: Appellation before grape (e.g., "Mendoza Malbec").
    - Bordeaux: Include "Grand Cru Classe" after Pauillac, Margaux, etc., if applicable.
    - **Never assume or fabricate any data, especially the vintage year. Only include it if it is clearly present and unambiguous in the extracted text.**
    - Return only the final cleaned, space-separated name.
"""
}
