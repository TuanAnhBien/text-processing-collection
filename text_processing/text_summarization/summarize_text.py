

def _summarize_text(words, start_idx, end_idx, each_side):
    kw_words = words[start_idx: end_idx + 1]
    left_words = words[end_idx + 1: end_idx + each_side + 1]
    right_words = words[-(len(words) - start_idx + each_side):start_idx]

    left_str = u" ".join(left_words)
    right_str = u" ".join(right_words)

    kw = u" ".join(kw_words)

    result = u" ".join([right_str, kw, left_str]).strip()

    if len(words) - end_idx - 1 > each_side:
        result += u" ..."
    if start_idx > each_side:
        result = u"... " + result

    return result


def summarize_text(text, max_num_words=30):
    words = text.split()

    if len(words) <= max_num_words:
        return text

    each_side = int(max_num_words / 2)

    # Calculate start and end index of keyword
    start_end_idx = []
    start_idx = -1
    end_idx = -1
    for idx, word in enumerate(words):
        if "<em>" in word:
            if start_idx < 0:
                start_idx = idx
            end_idx = idx
        elif start_idx > 0 and end_idx > 0:
            start_end_idx.append((start_idx, end_idx))
            start_idx = -1
            end_idx = -1

    # If no have any keyword in text
    if not start_end_idx and (start_idx == -1 or end_idx == -1):
        return u" ".join(words[:max_num_words - 1]) + u" ..."

    if not start_end_idx:
        start_end_idx.append((start_idx, end_idx))

    # If only have one keyword, summarize this keyword and return
    if len(start_end_idx) == 1:
        start, end = start_end_idx[0]
        return _summarize_text(words, start, end, each_side)

    # Merge these indies that close each other
    final_start_end = []
    cache_merge_idx = []
    for idx, start_end in enumerate(start_end_idx):
        if start_end in cache_merge_idx:
            continue

        start, end = start_end

        try:
            start_next, end_next = start_end_idx[idx + 1]
        except IndexError:
            final_start_end.append(start_end)
            break

        if start_next - end - 1 <= max_num_words:
            final_start_end.append((start, end_next))
            cache_merge_idx.append((start_next, end_next))
        else:
            final_start_end.append(start_end)

    # Summarize with multi keywords
    result = []
    for idx, start_end in enumerate(final_start_end):
        start, end = start_end
        sum_text = _summarize_text(
            words, start, end, each_side,
        )
        result.append(sum_text)

    return u" ".join(result).strip().replace("... ...", "...")
