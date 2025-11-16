def typing_time_analysis(code_lines, times):
    results = []
    fastest_char_time = 0.055  # seconds per character (fastest human typing speed)

    for line, t in zip(code_lines, times):
        chars = len(line)
        required_min_time = chars * fastest_char_time

        if t < required_min_time:
            results.append((line, "⚠ Pasted (Too Fast to Type)"))
        else:
            results.append((line, "✔ Typed Normally"))
    
    return results
