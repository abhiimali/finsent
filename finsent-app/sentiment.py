import streamlit as st
from newspaper import Article

from  stock_dict import stocks_dict
from  smallcase import get_small_case_data



def get_article_info(urls):
    total_para = []
    combined_paragraph = ""
    for url in urls:
        article = Article(url)
        article.download()
        article.parse()
        title = article.title
        description = article.meta_description
        summary = article.summary
        # Concatenate all paragraphs into one
        combined_paragraph += f"{title}\n{description}\n{summary}\n"
    
    # Append the combined paragraph to the list
    total_para.append(combined_paragraph.strip())

    return total_para

def get_sentiment_from_data(paragraph):
    from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
    
    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
    model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
    
    # Tokenize the paragraph with padding and truncation
    inputs = tokenizer(paragraph, padding=True, truncation=True, return_tensors="pt")
    
    # Initialize the pipeline
    pipe = pipeline("text-classification", model=model, tokenizer=tokenizer)
    
    # Perform sentiment analysis
    sentiment_result = pipe(paragraph)
    
    return sentiment_result

def display_sentiments(sentiment_results):
    st.subheader('Sentiment Analysis Results:')
    for i, sentiment_result in enumerate(sentiment_results):
        st.write(f"Result {i + 1}:")
        if sentiment_result['label'] == 'positive':
            st.success('Sentiment: Positive')
        elif sentiment_result['label'] == 'negative':
            st.error('Sentiment: Negative')
        else:
            st.info('Sentiment: Neutral')
        
def show_sentiment_analysis_page():
    # Add content for the Sentiment Analysis page
    st.title("Sentiment Analysis")
    selected_stock = st.selectbox("Select a stock", list(stocks_dict.keys()))
    
    urls , titles = get_small_case_data(selected_stock)
    paragraph = get_article_info(urls)
    print(paragraph)
    sentiment = get_sentiment_from_data(paragraph)

    print(sentiment)
    display_sentiments(sentiment)
    # st.write("Sentiment:", sentiment[0]['label'])

