import re
from word2number import w2n

def extract_range_or_single(number_match):
    if 'to' in number_match:
        numbers = number_match.split('to')
        return numbers[0]
    else:
        return convert_number_from_words(number_match)

def convert_number_from_words(number_string):
    # Split number string into components and try converting with word2number
    try:
        # Handle numeric abbreviations like '10K' or '1M'
        if 'k' in number_string.lower():
            return int(float(number_string.lower().replace('k', '')) * 1000)
        elif 'm' in number_string.lower():
            return int(float(number_string.lower().replace('m', '')) * 1000000)
        else:
            # Try converting directly if it's a simple number string
            if number_string.isdigit():
                return int(number_string)
            else:
                # Handle more complex worded numbers
                return w2n.word_to_num(number_string)
    except ValueError:
        return None
    

def assess_attainability(measurability, specificity, frequency):
    activity_scores = {
        "running": 8, "jogging": 7, "cycling": 6, "swimming": 8,
        "yoga": 4, "pilates": 4, "stretching": 3, "dancing": 5,
        "hiking": 7, "aerobics": 6, "elliptical": 5, "rowing": 6,
        "gardening": 3, "tai chi": 3
    }

    frequency_impact = {
        'daily': 10, 'weekdays': 8, 'monday - friday': 8,
        'monday - saturday': 9, 'weekly': 4, 'weekends': 3,
        'saturday and sunday': 3
    }

    base_score = activity_scores.get(specificity, 5)
    frequency_score = frequency_impact.get(frequency, 5)
    
    if measurability:
        try:
            value = int(measurability)
            if value > 1000:
                measurability_score = 10
            elif value > 500:
                measurability_score = 7
            else:
                measurability_score = 4
        except ValueError:
            measurability_score = 5
    else:
        measurability_score = 5

    total_score = (base_score + frequency_score + measurability_score) / 3
    attainability = round(total_score)
    return max(1, min(attainability, 10))

def extract_info(sentence):
    sentence = sentence.lower().replace(',', '').replace('-', ' to ')

     # Extended regex to capture complex word-based numbers more effectively
    num_pattern = r'\b((\d+(?:\.\d+)?[km]?|one|two|three|four|five|six|seven|eight|nine|ten|' \
                  r'eleven|twelve|thirteen|fourteen|fifteen|sixteen|' \
                  r'seventeen|eighteen|nineteen|twenty|thirty|forty|' \
                  r'fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion)+)\b'
    # Use regex to find all number-related words or groups
    number_matches = re.findall(num_pattern, sentence)
    numbers = []
    for match in number_matches:
        if isinstance(match, tuple):
            match = match[0]  # Extract the number string from regex groups
        number = convert_number_from_words(match)
        if number is not None:
            numbers.append(number)

    measurability = min(numbers) if numbers else None
    
    activities = [
        "steps", "jogging", "cycling", "swimming", 
        "yoga", "pilates", "stretching", "dancing", "hiking",
        "aerobics", "elliptical", "rowing", "gardening", "tai chi"
    ]
    activity_pattern = r'\b(' + '|'.join(activities) + r')\b'
    specificity_match = re.search(activity_pattern, sentence)
    specificity = specificity_match.group(0) if specificity_match else "Steps"

    frequency_patterns = {
        'Monday - Friday': r'\bweekdays\b|(monday to|monday through|monday -) friday',
        'Monday - Saturday': r'\b(monday to|monday through|monday -) saturday\b',
        'weekly': r'\bweekly\b|once a week|every week|each week|per week|weekly basis|throughout the week',
        'weekend': r'\bweekends?\b|on weekends?|(saturday and sunday|over the weekend)',
        'daily': r'\bdaily\b|every day|per day|each day|daily basis|every morning|every evening|every night|every afternoon'
    }

    frequency = None
    for key, pattern in frequency_patterns.items():
        if re.search(pattern, sentence):
            frequency = key
            break
    if not frequency:
        frequency = "daily"

    attainability = assess_attainability(measurability, specificity, frequency)
    
    return {
        "Measurability": str(measurability) if measurability else None,
        "Specificity": specificity,
        "Attainability": attainability,
        "Frequency": frequency
    }

# Test the function with example sentences
sentence = "Let's do 1000 steps every Monday to Friday."
info = extract_info(sentence)
print(info)

