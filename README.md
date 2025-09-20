# 🎬 Movie Recommendation System

This is a **Content-Based Movie Recommender Web App** that suggests movies based on a selected movie using cosine similarity on movie metadata like genres, keywords, cast, and crew.



---

## 📌 Features

- 🧠 Recommends 5 similar movies based on the movie you select
- 🎞️ Displays movie posters using TMDB API
- 📂 Efficiently handles large similarity matrices with cloud integration (Google Drive)
- 🚀 Deployed using **Streamlit Cloud** with GitHub integration

---

## 🛠️ Tech Stack

| Category | Technology |
|---------|------------|
| **Frontend** | Streamlit |
| **Backend** | Python |
| **Machine Learning** | Cosine Similarity |
| **Data Wrangling** | Pandas |
| **NLP** | NLTK (Stemming, Tokenization) |
| **Vectorization** | scikit-learn (`CountVectorizer`) |
| **Visualization** | TMDB Posters via API |
| **Deployment** | Streamlit Cloud + GitHub |
| **Storage** | Google Drive for large `.pkl` file |

---

## 🧪 Libraries Used

```bash
pandas
numpy
scikit-learn
nltk
requests
gdown
streamlit
