[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br /> 
<div align="center">
  <a href="https://github.com/akash85246/Skill2Salary-ml">
    <img src="./images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Skill2Salary-ml</h3>

  <p align="center">
    An awesome personal book review platform where user can share his reviews of books.
    <br />
    <a href="https://github.com/akash85246/Skill2Salary-ml/issues/new?labels=bug">Report Bug</a>
    ·
    <a href="https://github.com/akash85246/Skill2Salary-ml/issues/new?labels=enhancement">Request Feature</a>
    .
    <a href="https://github.com/akash85246/Skill2Salary-ml/blob/main/CONTRIBUTING.md">Contribute</a>
    .
    <a href="https://github.com/akash85246/Skill2Salary-ml/pulls">Pull Requests</a>
    .
    <a href="https://github.com/akash85246/Skill2Salary-ml/security">Report Security Issue</a>
    .
    <a href="https://github.com/akash85246/Skill2Salary-ml/fork">Fork the Project</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#behind-the-scenes">Behind the Scenes</a></li>
    <li><a href="#tips-for-better-predictions">Tips for Better Predictions</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://skill2salary.streamlit.app/)

Skill2Salary is a smart salary prediction platform designed to help users estimate their expected salary based on educational background, work experience, and job preferences. Powered by machine learning, the app uses real-world data to make informed predictions and guide users in career planning.

### Features

- **Salary Prediction Engine**: Predicts salaries based on user input such as education, experience, job level, and location.
- **Advanced Ensemble Models**: Utilizes ensemble techniques like Stacking, Random Forest, and Gradient Boosting for robust predictions.
- **Hyperparameter Tuning**: Implements both GridSearchCV and RandomizedSearchCV to optimize model performance.
- **Streamlit-Based UI**: Clean and interactive user interface built entirely with Streamlit for real-time predictions.
- **Categorical Feature Encoding**: Uses `OrdinalEncoder` with controlled category ordering and handles unknown categories gracefully.
- **Feature Engineering**: Includes derived metrics like experience buckets, combined experience score, and average academic score for improved accuracy.
- **Log-Salary Handling**: Trained on log-transformed salary data to handle skewed distributions, with inverse transformation for final output.
- **Responsive Input Forms**: Organizes user inputs into logical sections (education, job, company) for a better user experience.
- **Lightweight and Fast**: No authentication, no database—runs purely as a lightweight local or cloud-hosted app.
- **Deployment Ready**: Easily deployable on platforms like Render, HuggingFace Spaces, or Streamlit Cloud.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

Built with cutting-edge technologies to deliver performance and reliability.

* [![Python][Python]][Python-url]
* [![Pandas][Pandas]][Pandas-url]
* [![Scikit-Learn][Sklearn]][Sklearn-url]
* [![Streamlit][Streamlit]][Streamlit-url]
* [![NumPy][Numpy]][Numpy-url]
* [![Matplotlib][Matplotlib]][Matplotlib-url]
* [![Git][Git]][Git-url]
* [![GitHub][GitHub]][GitHub-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Get started quickly with these easy setup instructions.

### 🛠️ Prerequisites

Before you begin, make sure you have the following installed and configured:

- **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
- **pip**: Comes pre-installed with Python. Used to install Python packages.
- **Streamlit**: Install using `pip install streamlit` ([Streamlit Docs](https://docs.streamlit.io/))
- **Scikit-learn**: Install using `pip install scikit-learn`
- **Pandas & NumPy**: Install using `pip install pandas numpy`
- **Matplotlib or Seaborn** *(optional)*: For data visualization  
  `pip install matplotlib seaborn`
- **Git**: [Download Git](https://git-scm.com/) to clone the repository or manage version control
- **Jupyter Notebook** *(optional)*: For experimentation before deployment  
  `pip install notebook`

#### Recommended Knowledge

To make the most out of this project, it helps to be familiar with:

- **Machine Learning Concepts**
- **Data Preprocessing & Feature Engineering**
- **Python & Pandas**
- **Model Evaluation & Hyperparameter Tuning**

### 🚀 Installation

Follow these steps to set up the **Skill2Salary** project locally:

---

1. **Clone the Repository**

```bash
git clone https://github.com/akash85246/Skill2Salary-ml.git
cd Skill2Salary-ml
```

---

2. **Create and Activate a Virtual Environment** (Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

---

3. **Install Python Dependencies**

```bash
pip install -r requirements.txt
```

> If you don’t have a `requirements.txt`, install manually:

```bash
pip install streamlit pandas numpy scikit-learn
```

---

4. **Ensure Model Artifacts are Present**

Make sure the following files are inside the `model/` directory:

- `model.pkl` – Trained ensemble model
- `oe.pkl` – OrdinalEncoder used during training
- `selector.pkl` – Feature selector (e.g., SelectKBest)
- `columns.pkl` – List of columns used during training

> These files are required for prediction and must match the training pipeline.

---

5. **Run the Streamlit App**

```bash
streamlit run app.py
```

---

6. **(Optional)**: Explore the Jupyter Notebooks for Training & Tuning

```bash
jupyter notebook
```

You can explore training workflows like feature selection, model tuning (GridSearchCV, RandomizedSearchCV), and ensemble building.

---

📌 **Note**: This project doesn't require any database or authentication setup. It's a lightweight, ML-powered web app built purely with **Streamlit** for UI and **scikit-learn** for prediction.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE -->
## 📈 Usage

Using the **Skill2Salary** application is simple and intuitive. Here's how to get started:

---

### 🎯 Predicting Your Salary

1. **Launch the App**
   ```bash
   streamlit run app.py
   ```

2. **Fill in Your Details**  
   Provide your:
   - Education level  
   - 10th and 12th grade marks  
   - College CGPA  
   - Work experience in years  
   - Job seniority level  
   - Company size and location  
   - Year you started working  

3. **Click on the "🔍 Predict Salary" Button**  
   The model processes your input and returns a salary estimate based on advanced ensemble regression models.

---
<!-- Behind the Scenes -->
##  Behind the Scenes

- The app uses a **Stacked Ensemble Regressor** trained on industry-level salary datasets.
- Features are processed using:
  - `OrdinalEncoder` with predefined categories.
  - `SelectKBest` for feature selection.
- **Log-transformed salaries** are predicted and converted back using `np.expm1()` for more accurate skewed distribution modeling.

---
<!-- Tips for Better Predictions -->
## Tips for Better Predictions

- Use real or realistic inputs to get meaningful results.
- The model was trained with robust hyperparameter tuning (GridSearchCV and RandomizedSearchCV).
- Try different combinations of job roles and experience levels to understand how they affect salary.

---

<p align="right">(<a href="#readme-top">back to top</a>)</p>



See the [open issues](https://github.com/akash85246/Skill2Salary-ml/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. **Fork the Project**
   - Click the "Fork" button at the top-right corner of this page to create a copy of the repository in your GitHub account.

2. **Clone the Repository**
   - Clone your forked repository to your local machine:
     ```bash
     git clone https://github.com/your-username/Skill2Salary-ml.git
     ```

3. **Create Your Feature Branch**
   - Navigate to your project folder and create a new branch for your feature:
     ```bash
     git checkout -b feature/AmazingFeature
     ```

4. **Commit Your Changes**
   - After making the necessary changes, commit them:
     ```bash
     git commit -m 'Add some AmazingFeature'
     ```

5. **Push to the Branch**
   - Push your changes to your forked repository:
     ```bash
     git push origin feature/AmazingFeature
     ```

6. **Open a Pull Request**
   - Go to the original repository (`akash85246/Skill2Salary-ml`), and open a pull request to merge your feature branch into the `main` branch.
   - Provide a brief description of the changes you've made and submit the pull request for review.

### Top contributors:

<a href="https://github.com/akash85246/Skill2Salary-ml/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=akash85246/Skill2Salary-ml" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Akash Rajput - [@akash_rajp91025](https://x.com/akash_rajp91025) - akash.rajput.dev@gmail.com

Project Link: [https://github.com/akash85246/Skill2Salary-ml](https://github.com/akash85246/Skill2Salary-ml)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/akash85246/Skill2Salary-ml.svg?style=for-the-badge
[contributors-url]: https://github.com/akash85246/Skill2Salary-ml/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/akash85246/Skill2Salary-ml.svg?style=for-the-badge
[forks-url]: https://github.com/akash85246/Skill2Salary-ml/network/members
[stars-shield]: https://img.shields.io/github/stars/akash85246/Skill2Salary-ml.svg?style=for-the-badge
[stars-url]: https://github.com/akash85246/Skill2Salary-ml/stargazers
[issues-shield]: https://img.shields.io/github/issues/akash85246/Skill2Salary-ml.svg?style=for-the-badge
[issues-url]: https://github.com/akash85246/Skill2Salary-ml/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/akash-rajput-68226833a/
[product-screenshot]: images/homepage.png

[Python]: https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[Pandas]: https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/

[Sklearn]: https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white
[Sklearn-url]: https://scikit-learn.org/

[Streamlit]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[Streamlit-url]: https://streamlit.io/

[Numpy]: https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white
[Numpy-url]: https://numpy.org/

[Matplotlib]: https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white
[Matplotlib-url]: https://matplotlib.org/

[Git]: https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white
[Git-url]: https://git-scm.com/

[GitHub]: https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white
[GitHub-url]: https://github.com/
