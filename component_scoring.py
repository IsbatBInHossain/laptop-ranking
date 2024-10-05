import re

# RAM scoring
def score_ram(ram):
    return min(ram / 2, 10)

# Storage scoring based on type and capacity
def score_storage(storage_type, capacity):
    score = 2 + (3 if 'ssd' in storage_type.lower() else 0) + min(capacity / 128, 5)
    return min(score, 10)

# Graphics scoring
def score_graphics(graphics):
    graphics = str(graphics).lower()
    graphics_scores = {
        'rtx': 10, 'gtx': 8, 'nvidia': 7,
        'radeon': 6, 'intel iris': 5, 'intel uhd': 4
    }
    for key, score in graphics_scores.items():
        if key in graphics:
            return score
    return 3

# Screen size extraction and scoring
def extract_screen_size(size_str):
    match = re.search(r'(\d+\.?\d*)', str(size_str))
    return float(match.group(1)) if match else 0

def score_screen(size_str):
    return min((extract_screen_size(size_str) / 2) + 2, 10)

def score_price(price, tolerance, min_price, max_price):

    normalized_price = (price - min_price) / (max_price - min_price)

    if price <= tolerance:
        # The lower the price compared to tolerance, the better the score
        score = 10 * (1 - normalized_price)  # Score is better when price is lower
    else:
        # The higher the price compared to tolerance, the more penalty applied
        penalty = (price - tolerance) / tolerance
        score = max(0, 10 * (1 - normalized_price) - penalty * 10) 
    # Ensure score is between 0 and 10
    return max(0, min(10, score))