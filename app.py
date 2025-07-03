import gradio as gr
from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Define summarization function
def summarize_text(text):
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]["summary_text"]

# Define Gradio interface
title = "📝 SmartSummarizer – Real-Time Text Summarization App"

user_instructions = """
Welcome to SmartSummarizer! ✨  
Paste a paragraph, article, or long-form English content (ideally 50–300 words).  
The model will return a short, readable summary.  
✅ Best for **news**, **science**, **education**, **business**, or **blog-style** content.  
🌐 Model works only with English input.  
⚠️ Avoid one-liners or grammatically broken input.
"""

# Placeholder example
example_text = """Artificial intelligence is transforming industries by automating tasks, 
improving decision-making, and creating new opportunities in sectors such as healthcare, 
finance, and transportation. However, experts caution that without proper regulation, 
AI could also lead to job displacement, bias in decision-making systems, 
and ethical concerns regarding data privacy and accountability."""

# Launch interface
demo = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=15, placeholder="Paste your article or paragraph here...", label="Enter Text to Summarize"),
    outputs=gr.Textbox(label="Generated Summary"),
    title=title,
    description=user_instructions,
    examples=[[example_text]],
)

if __name__ == "__main__":
    demo.launch()

