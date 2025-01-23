import streamlit as st

# Title of the Resume
st.title("Nitu Yadav's Digital Resume")

# Introduction
st.subheader("About Me")
st.write("""
Hi, I'm Nitu Yadav, a passionate Software Engineer with 2 years of experience in developing scalable web applications.
I specialize in Python, JavaScript, and cloud technologies. My goal is to build innovative products that solve real-world problems.
""")

# Skills Section
st.subheader("Skills")
skills = [
    "Python", "JavaScript", "HTML/CSS", "MySQL", "Kubernetes", "AWS", "Docker", "SQL"
]
st.write("Here are my key skills:")
for skill in skills:
    st.write(f"- {skill}")

# Experience Section
st.subheader("Experience")

st.write("### Software Engineer at Tech Company")
st.write("""
- Designed and implemented scalable web applications using Python, Flask, and React.
- Led the migration of legacy systems to AWS, reducing costs by 30%.
- Collaborated with cross-functional teams to deliver high-impact features.
""")

st.write("### Web Developer at Web Solutions")
st.write("""
- Developed and maintained e-commerce websites using JavaScript, Node.js, and MongoDB.
- Improved website performance by optimizing front-end code and APIs.
- Provided technical support and resolved issues for clients.
""")

# Education Section
st.subheader("Education")
st.write("### Bachelor of Computer Applications")
st.write("University of IGNOU - Graduated: 2020")
st.write("### Master's of Computer Appilications")
st.write("University of GGSIPU - Post Graduated: 2023")
st.write("Courses: Data Structures, Algorithms, Machine Learning, Web Development")

# Projects Section
st.subheader("Projects")

st.write("### Web Scraper Application")
st.write("""
- Built a Python web scraper to collect and analyze data from websites.
- Stored the data in a structured format and generated reports.
- [GitHub Repository](https://github.com/johndoe/web-scraper)
""")

st.write("### E-Commerce Website")
st.write("""
- Developed a fully functional e-commerce website with user authentication, shopping cart, and payment integration.
- [Live Demo](https://www.example.com)
""")

# Contact Information Section
st.subheader("Contact")
st.write("You can reach me at:")
st.write("Email: nitu.yadav@nashtechglobal.com")
st.write("LinkedIn: [Nitu Yadav](https://www.linkedin.com/in/nituyadav)")
st.write("GitHub: [nituyadav](https://github.com/nituyadav0109)")

# Displaying a Profile Picture
st.image("pic.jpg", width=200)
