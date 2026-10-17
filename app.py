import streamlit as st


def compress_rle(text: str) -> str:
    """Compress consecutive repeated characters using Run-Length Encoding."""
    if not text:
        return ""

    parts = []
    current = text[0]
    count = 1

    for char in text[1:]:
        if char == current:
            count += 1
        else:
            parts.append(f"{count}{current}")
            current = char
            count = 1

    parts.append(f"{count}{current}")
    return "".join(parts)


st.set_page_config(
    page_title="RLE Text Compressor",
    page_icon="🗜️",
    layout="centered",
)

st.title("🗜️ RLE Text Compressor")
st.write(
    "Compress consecutive repeated characters with "
    "**Run-Length Encoding (RLE)**."
)

input_text = st.text_area(
    "Enter text to compress",
    value="aaabbccccd",
    height=140,
    placeholder="For example: aaabbccccd",
    help="Spaces, punctuation, and line breaks are treated as characters too.",
)

if st.button("Compress text", type="primary", use_container_width=True):
    if input_text == "":
        st.warning("Enter some text first so there is something to compress.")
    else:
        compressed = compress_rle(input_text)
        original_length = len(input_text)
        compressed_length = len(compressed)
        size_ratio = (compressed_length / original_length) * 100
        change = original_length - compressed_length

        st.subheader("Results")
        col1, col2 = st.columns(2)
        col1.metric("Original length", f"{original_length} characters")
        col2.metric("Compressed length", f"{compressed_length} characters")

        st.text_area(
            "Compressed output",
            value=compressed,
            height=100,
            disabled=True,
        )

        if change > 0:
            st.success(
                f"Output is {change} characters shorter "
                f"({100 - size_ratio:.1f}% smaller by character count)."
            )
        elif change < 0:
            st.info(
                f"Output is {abs(change)} characters longer. "
                "RLE works best when characters repeat in consecutive runs."
            )
        else:
            st.info("The original and compressed strings have the same length.")

        st.caption(
            "Note: This is a learning demonstration. Character count is not "
            "the same as actual file size in bytes, and this simple format "
            "is not unambiguous for every possible input."
        )

with st.expander("How does RLE work?"):
    st.markdown(
        """
        1. Read the input from left to right.
        2. Count each run of consecutive identical characters.
        3. Write the count followed by the character.
        4. Join the groups to produce the encoded output.

        **Example:** `aaabbccccd` → `3a2b4c1d`
        """
    )
