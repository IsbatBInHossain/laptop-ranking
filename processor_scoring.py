import re

def score_processor_type(processor):
    processor = processor.lower()
    processor_scores = {
        'i9': 10, 'ryzen 9': 10, 'threadripper': 10,
        'i7': 9, 'ryzen 7': 9,
        'i5': 7, 'ryzen 5': 7,
        'i3': 5, 'ryzen 3': 5,
        'xeon': 8, 'epyc': 8,
        'pentium': 4, 'athlon': 4, 'celeron': 4
    }
    for key, score in processor_scores.items():
        if key in processor:
            return score
    return 3  # Default score for unknown processors

def score_intel_processor(gen):
    intel_patterns = [
        (r'(\d+)(?:th|rd|nd|st)?\s*(gen|processor)', lambda m: int(m.group(1))),
        (r'core[- ](?:ultra[- ]?)?(?:[ium][3579]|5)[- ](\d{2})(\d{3})[a-z]*', lambda m: int(m.group(1))),
        (r'core[- ](?:ultra[- ]?)?(?:[ium][3579]|5)[- ](\d)(\d{2,3})[a-z]*', lambda m: int(m.group(1))),
        (r'core[- ](?:ultra[- ]?)?([ium][3579])(?![- ]\d)', lambda m: {'i3': 3, 'i5': 5, 'i7': 7, 'i9': 9}.get(m.group(1).lower(), 0)),
    ]

    if 'celeron' in gen:
        return 2
    if 'pentium' in gen:
        return 3

    for pattern, gen_func in intel_patterns:
        match = re.search(pattern, gen)
        if match:
            try:
                gen_num = gen_func(match)
                if 1 <= gen_num <= 14:
                    return min(gen_num - 3, 10)
            except (ValueError, IndexError, KeyError):
                continue

    return 0

def score_amd_processor(gen):
    ryzen_patterns = [
        r'ryzen[- ](\d+)[- ]?(\d{4})',
        r'ryzen[- ](\d+)[- ]?pro[- ]?(\d{4})',
        r'ryzen[- ](\d+)',
    ]
    
    for pattern in ryzen_patterns:
        ryzen_match = re.search(pattern, gen)
        if ryzen_match:
            try:
                gen_num = int(ryzen_match.group(2)[0]) if len(ryzen_match.groups()) == 2 else int(ryzen_match.group(1)[0])
                return min(gen_num * 1.375, 10)
            except ValueError:
                continue
    return 0

def score_apple_processor(gen):
    m_series = re.search(r'm(\d+)', gen)
    if m_series:
        gen_num = int(m_series.group(1))
        return min(gen_num * 3, 10)
    return 0


def score_by_core_count(gen):
    core_patterns = [
        r'(\d+)[ -]?(?:core|quad|duo)',
        r'(dual|quad)[ -]?core',
    ]
    
    for pattern in core_patterns:
        core_match = re.search(pattern, gen)
        if core_match:
            try:
                if core_match.group(1).isdigit():
                    cores = int(core_match.group(1))
                else:
                    cores = 2 if core_match.group(1) == 'dual' else 4
                return min(cores - 1, 10)
            except ValueError:
                continue
    return 0