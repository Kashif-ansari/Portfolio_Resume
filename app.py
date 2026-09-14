"""Portfolio application foundation.

Update PORTFOLIO_DATA with your content before building page sections or RAG features.
"""

import streamlit as st
import streamlit.components.v1 as components
from html import escape
from base64 import b64encode
import json
from mimetypes import guess_type
from pathlib import Path


# =============================================================================
# PORTFOLIO_DATA — EDIT THIS SECTION WITH YOUR ACTUAL PORTFOLIO CONTENT
# =============================================================================
PORTFOLIO_DATA = {
    "identity": {
        "name": "Muhammad Kashif Ansari",  # e.g. "Jane Doe"
        "title": "AI Engineer | Computer Vision | ML Engineer",  # Edit headline
        "summary": (
            "I am a Data Scientist, AI/ML Engineer, and Computer Vision Engineer passionate about turning data and intelligent technologies into practical, impactful solutions. My experience combines machine learning, deep learning, computer vision, data analysis, and software development. I have worked on projects including a deep-learning-based polyp detection system using CNNs, TensorFlow, OpenCV, and fuzzy logic, as well as data-driven applications such as Stockifistic. My academic and professional journey, along with my experience as a Computer Science Lab Instructor, has strengthened both my technical expertise and problem-solving abilities."
            "I am continuously learning and exploring modern AI technologies, including RAG, LLMs, AI engineering, model optimization, and deployment. Moving forward, my goal is to grow as an AI/ML professional by solving challenging real-world problems, contributing to meaningful research, and building intelligent systems that create measurable impact. I am driven by curiosity, continuous learning, and a passion for transforming innovative ideas into reliable, real-world AI solutions."
        ),  # Edit professional summary
        "location": "Karachi, Pakistan",  # Optional
        "profile_image": "assets/profile.jpg",  # Local path or hosted image URL
        "bio": "My professional journey has grown from a foundation in software development and computer science into a focused career in Data Science, Artificial Intelligence, Machine Learning, and Computer Vision. Through academic study, professional software development, university teaching, and hands-on research, I have gained experience building practical solutions while continuously strengthening my understanding of emerging technologies. From developing software applications to researching deep-learning-based computer vision systems, I enjoy turning complex problems into meaningful and usable solutions. My core values are continuous learning, innovation, problem-solving, integrity, and practical impact. I believe technology is most valuable when it solves real problems and creates measurable value. Moving forward, I aim to build a career as an AI/ML Engineer and Data Scientist, specializing in intelligent systems, computer vision, and AI engineering. I am committed to continuously expanding my technical expertise, contributing to impactful research and projects, and transforming emerging AI technologies into reliable solutions for real-world challenges.",
        "currently_learning": ["Custom and Distributed Training with TensorFlow", "Generative Deep Learning with TensorFlow", "Custom Models, Layers, and Loss Functions with TensorFlow"],  # Edit topics
        "development_process": ["Discover", "Design", "Build", "Iterate"],  # Edit process
    },
    "experience": [
        {
            "company": "Mohammad Ali Jinnah University",  # Edit company
            "role": "Lab Instructor",  # Edit role
            "date_range": "09 2025 – Present",  # Edit dates
            "location": "Karachi, Pakistan",  # Optional
            "achievements": [
                "Successfully delivered Data Communication & Networks and Operating Systems laboratory sessions, providing hands-on learning in networking, Linux, C, Bash, and system concepts.",
    "Served as FYP Coordinator and Teaching Assistant, supporting student assessments, coordinating FYP activities, and guiding student groups throughout their projects."

            ],
        },
        {
            "company": "Koder Labs",  # Edit company
            "role": "Dot Net Developer",  # Edit role
            "date_range": "10 2024 – 08 2025",  # Edit dates
            "location": "Karachi, Pakistan",  # Optional
            "achievements": [
                "Developed and maintained web applications using C#, ASP.NET, SQL, HTML, and CSS, contributing to reliable and scalable software solutions.",
    "Worked across database development, application deployment, and hosting, strengthening full-stack development and production support skills."
],
        },
        {
                    "company": "Atique Trading Co",  # Edit company
                    "role": "IT Administration",  # Edit role
                    "date_range": "01 2023 – 12 2023",  # Edit dates
                    "location": "Karachi, Pakistan",  # Optional
                    "achievements": [
                        "Managed and maintained IT infrastructure, computer systems, networks, and software to ensure smooth and reliable day-to-day operations.",
"Provided technical support, troubleshooting, system maintenance, and user assistance while helping improve overall IT efficiency and security."],
        },
    ],
    "education": [
        {
            "degree": "M.S. in Data Science",  # Edit degree
            "institution": "Mohammad Ali Jinnah University",  # Edit institution
            "graduation_year": "2027",  # Edit year
            "coursework": ["Machine Learning", "Computer Vision","Data Science"],  # Edit courses
        },
        {
            "degree": "B.S. in Computer Science",  # Edit degree
            "institution": "Karachi institute of economics and Technology",  # Edit institution
            "graduation_year": "2024",  # Edit year
            "coursework": ["Machine Learning", "Data Structures"],  # Edit courses
        },
        {
            "degree": "Pre-Engineering",  # Edit degree
            "institution": "Sindh Muslim Science college",  # Edit institution
            "graduation_year": "2020",  # Edit year
            "coursework": ["Mathematics", "Statistics"],  # Edit courses
        },
    ],
    "projects": [
        {
            "title": "Project Title",  # Edit project name
            "category": "Machine Learning",  # e.g. AI, Web App, Computer Vision
            "year": "YYYY",  # Edit year
            "tools": ["Python", "Streamlit", "FAISS"],  # Edit stack
            "role": "AI Engineer",  # Edit role: Computer Vision, Data Scientist, ML Engineer
            "overview": "Describe the problem, solution, and outcome.",  # Edit overview
            "process_notes": "Add implementation notes, progress, or WIP details.",
            "image": "assets/project-image.jpg",  # Local path or hosted image URL
            "concept_reference": "Add mood-board, reference, or architecture-diagram notes.",
            "concept_images": [],  # Add local/remote image paths for mood boards or diagrams
            "wip_images": [],  # Add local/remote implementation or progress images
            "live_demo_url": "https://example.com",  # Optional live demo
            "repository_url": "https://github.com/your-username/project",  # Optional repo
        },
    ],
    "certificates": [
        # Add exactly 9 certificate entries when ready.
        {"title": "Python for Data Science ", "image": "assets/certificates/cert-01.jpg"},
        {"title": "Data Analysis with Python", "image": "assets/certificates/cert-02.jpg"},
        {"title": "Data Visualisation with Python", "image": "assets/certificates/cert-03.jpg"},
        {"title": "Machine Learning with Python", "image": "assets/certificates/cert-04.jpg"},
        {"title": "Pytorch: Tensor, Data Set and Augmentation", "image": "assets/certificates/cert-05.jpg"},
        {"title": "Deep Learning Fundamentals ", "image": "assets/certificates/cert-06.jpg"},
        {"title": "Deep Learning with TensorFlow", "image": "assets/certificates/cert-07.jpg"},
        {"title": "Accelerative Deep Learning with GPU’s", "image": "assets/certificates/cert-08.jpg"},
        {"title": "Deep Learning with PyTorch: Image Segmentation", "image": "assets/certificates/cert-09.jpg"},
        {"title": "Docker Essentials: A Developer Introduction", "image": "assets/certificates/cert-09.jpg"},
        {"title": "Introduction to Containers, Kubernetes, and OpenShift", "image": "assets/certificates/cert-09.jpg"},
        
    ],
    "skills": {
        "languages": ["Python","C#",],  # Edit languages
        "machine_learning": ["PyTorch", "TensorFlow", "scikit-learn","Matplotlib"],
        "tools_and_frameworks": ["Streamlit", "FAISS", "OpenCV", "Git"],
        "databases": ["SQL", "Firebase"],
    },
    "contact": {
        "email": "mkashifansari579@gmail.com",  # Edit email
        "linkedin": "https://www.linkedin.com/in/muhammad-kashif-ansari-842b22159/",  # Edit LinkedIn URL
        "github": "https://github.com/Kashif-ansari",  # Edit GitHub URL
        "whatsapp": "https://wa.me/923308342284",  # Use country code, no + or spaces
        "discord": "your_discord_username",  # Edit Discord handle/invite URL
        "commission_status": "Available",  # e.g. Available, Limited, Unavailable
        "resume_path": "assets/resume.pdf",  # Local PDF path for the download button
    },
}


def inject_custom_css() -> None:
    """Inject global visual tokens and reusable portfolio component styles."""
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

            :root {
                --background: #0E1117;
                --surface: #151A23;
                --surface-raised: #1B2230;
                --border: rgba(148, 163, 184, 0.16);
                --text: #F8FAFC;
                --muted: #94A3B8;
                --neon-blue: #38BDF8;
                --neon-purple: #A78BFA;
                --gradient: linear-gradient(135deg, #38BDF8 0%, #8B5CF6 100%);
            }

            html, body, [class*="css"] {
                font-family: 'DM Sans', sans-serif;
            }

            .stApp {
                background:
                    radial-gradient(circle at 12% 5%, rgba(56, 189, 248, 0.10), transparent 30rem),
                    radial-gradient(circle at 88% 18%, rgba(139, 92, 246, 0.10), transparent 28rem),
                    var(--background);
                color: var(--text);
            }

            .block-container {
                max-width: 1180px;
                padding-top: 3rem;
                padding-bottom: 4rem;
            }

            h1, h2, h3, h4 {
                font-family: 'Space Grotesk', sans-serif !important;
                color: var(--text) !important;
                letter-spacing: -0.025em;
            }

            p, li, .stMarkdown {
                color: var(--muted);
                line-height: 1.7;
            }

            .portfolio-card {
                background: linear-gradient(145deg, rgba(27, 34, 48, 0.92), rgba(21, 26, 35, 0.92));
                border: 1px solid var(--border);
                border-radius: 18px;
                padding: 1.5rem;
                box-shadow: 0 12px 40px rgba(0, 0, 0, 0.20);
                transition: transform 180ms ease, border-color 180ms ease, box-shadow 180ms ease;
            }

            .portfolio-card:hover {
                transform: translateY(-4px);
                border-color: rgba(56, 189, 248, 0.45);
                box-shadow: 0 18px 48px rgba(56, 189, 248, 0.10);
            }

            .accent-text {
                background: var(--gradient);
                -webkit-background-clip: text;
                background-clip: text;
                color: transparent !important;
            }

            .skill-pill {
                display: inline-block;
                margin: 0.25rem 0.35rem 0.25rem 0;
                padding: 0.38rem 0.75rem;
                border: 1px solid rgba(167, 139, 250, 0.36);
                border-radius: 999px;
                background: rgba(139, 92, 246, 0.10);
                color: #DDD6FE;
                font-size: 0.84rem;
                font-weight: 600;
            }

            .stButton > button {
                border: 0;
                border-radius: 10px;
                background: var(--gradient);
                color: #FFFFFF;
                font-family: 'DM Sans', sans-serif;
                font-weight: 700;
                padding: 0.62rem 1rem;
                transition: transform 180ms ease, box-shadow 180ms ease;
            }

            .stButton > button:hover {
                border: 0;
                color: #FFFFFF;
                transform: translateY(-2px);
                box-shadow: 0 10px 24px rgba(56, 189, 248, 0.26);
            }

            [data-testid="stSidebar"] {
                background: rgba(14, 17, 23, 0.96);
                border-right: 1px solid var(--border);
            }

            hr {
                border-color: var(--border);
            }

            .project-card {
                overflow: hidden;
                min-height: 290px;
                margin-bottom: 0.65rem;
                border: 1px solid var(--border);
                border-radius: 18px;
                background: var(--surface);
                box-shadow: 0 12px 36px rgba(0, 0, 0, 0.18);
                transition: transform 180ms ease, border-color 180ms ease, box-shadow 180ms ease;
            }

            .project-card:hover {
                transform: translateY(-5px);
                border-color: rgba(56, 189, 248, 0.5);
                box-shadow: 0 20px 44px rgba(56, 189, 248, 0.10);
            }

            .project-card-image {
                display: block;
                width: 100%;
                height: 205px;
                object-fit: cover;
                background: var(--surface-raised);
            }

            .project-card-body { padding: 1rem 1.1rem 1.15rem; }
            .project-card-body h3 { margin: 0.55rem 0 0; font-size: 1.15rem; }
            .project-category, .project-meta span {
                display: inline-block;
                padding: 0.28rem 0.58rem;
                border: 1px solid rgba(56, 189, 248, 0.30);
                border-radius: 999px;
                background: rgba(56, 189, 248, 0.09);
                color: #BAE6FD;
                font-size: 0.72rem;
                font-weight: 700;
            }

            .project-detail-title { margin-bottom: 0.75rem; font-size: clamp(2.1rem, 5vw, 4.2rem); }
            .project-meta { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 0 0 1.5rem; }
            .project-meta span:nth-child(2) { border-color: rgba(167, 139, 250, 0.36); background: rgba(139, 92, 246, 0.10); color: #DDD6FE; }
            .project-meta span:nth-child(3) { border-color: rgba(45, 212, 191, 0.30); background: rgba(45, 212, 191, 0.08); color: #99F6E4; }
            .tool-label { margin: 0 0 0.35rem; color: var(--text) !important; font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; }
            .tool-list { margin-bottom: 2rem; }

            .certificate-card {
                position: relative; overflow: hidden; aspect-ratio: 1.28 / 1;
                border: 1px solid var(--border); border-radius: 14px; background: var(--surface-raised);
                box-shadow: 0 10px 28px rgba(0, 0, 0, .18);
            }
            .certificate-card img { display: block; width: 100%; height: 100%; object-fit: cover; transition: transform .35s ease, filter .35s ease; }
            .certificate-card:hover img { transform: scale(1.10); filter: brightness(.66); }
            .certificate-card span { position: absolute; left: 0; right: 0; bottom: 0; padding: 1rem .8rem .75rem; color: white; font-size: .82rem; font-weight: 700; background: linear-gradient(transparent, rgba(14,17,23,.92)); }
            .profile-frame { padding: .45rem; border: 1px solid rgba(56, 189, 248, .55); border-radius: 22px; background: linear-gradient(135deg, rgba(56,189,248,.22), rgba(139,92,246,.25)); box-shadow: 0 16px 44px rgba(56,189,248,.12); }
            .profile-frame img { display: block; width: 100%; border-radius: 17px; aspect-ratio: .84; object-fit: cover; background: var(--surface-raised); }
            .availability-list { display: flex; flex-wrap: wrap; gap: .5rem; margin: 1rem 0 1.5rem; }
            .availability-badge { padding: .4rem .75rem; border: 1px solid rgba(45,212,191,.32); border-radius: 999px; background: rgba(45,212,191,.08); color: #99F6E4; font-size: .82rem; font-weight: 700; }
            .proficiency-row { margin: .72rem 0; }
            .proficiency-label { display: flex; justify-content: space-between; margin-bottom: .3rem; color: #CBD5E1; font-size: .86rem; font-weight: 600; }
            .proficiency-track { height: 7px; overflow: hidden; border-radius: 99px; background: #273244; }
            .proficiency-fill { height: 100%; border-radius: inherit; background: var(--gradient); }
            .contact-panel { padding: 2rem; border: 1px solid var(--border); border-radius: 18px; text-align: center; background: linear-gradient(145deg, rgba(27,34,48,.94), rgba(21,26,35,.94)); }
            .contact-panel h2 { margin-top: 0; }
            .social-button { display: inline-block; margin: .3rem; padding: .62rem .9rem; border: 1px solid var(--border); border-radius: 9px; background: rgba(255,255,255,.03); color: #E2E8F0 !important; text-decoration: none; font-size: .9rem; font-weight: 700; transition: border-color .2s ease, transform .2s ease; }
            .social-button:hover { transform: translateY(-2px); border-color: var(--neon-blue); color: #fff !important; }
            .status-open { display: inline-block; margin: .75rem 0; padding: .45rem .8rem; border-radius: 999px; background: rgba(34,197,94,.1); color: #86EFAC; font-size: .88rem; font-weight: 700; }
            .site-footer { margin-top: 3.5rem; padding-top: 1.5rem; border-top: 1px solid var(--border); color: var(--muted); text-align: center; font-size: .82rem; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_hero_section() -> None:
    """Render a full-bleed interactive Three.js portfolio hero."""
    components.html(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <style>
                * { box-sizing: border-box; }
                html, body { margin: 0; width: 100%; height: 100%; overflow: hidden; }
                body { background: #0E1117; font-family: Arial, sans-serif; }
                #hero { position: relative; width: 100%; height: 100vh; min-height: 620px; overflow: hidden; background: #0E1117; }
                #webgl-canvas { position: absolute; inset: 0; display: block; width: 100%; height: 100%; }
                #hero::after {
                    content: ""; position: absolute; inset: 0; pointer-events: none;
                    background: radial-gradient(circle at center, transparent 0%, rgba(14, 17, 23, 0.18) 55%, rgba(14, 17, 23, 0.82) 100%);
                }
                .hero-content {
                    position: relative; z-index: 1; height: 100%; display: flex; flex-direction: column;
                    align-items: center; justify-content: center; padding: 2rem; text-align: center; color: #F8FAFC;
                }
                .eyebrow { margin: 0 0 1rem; color: #38BDF8; font-size: 0.78rem; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; }
                h1 { margin: 0; font-size: clamp(3rem, 8vw, 7rem); line-height: 0.94; letter-spacing: -0.065em; font-weight: 800; }
                .title { margin: 1.35rem 0 0; color: #DDD6FE; font-size: clamp(1rem, 2vw, 1.35rem); font-weight: 600; letter-spacing: 0.015em; }
                .tagline { max-width: 640px; margin: 1rem 0 2rem; color: #CBD5E1; font-size: clamp(1rem, 1.6vw, 1.15rem); line-height: 1.65; }
                .cta {
                    display: inline-flex; align-items: center; gap: 0.6rem; padding: 0.85rem 1.3rem; border: 1px solid rgba(255,255,255,.18);
                    border-radius: 999px; background: linear-gradient(135deg, #38BDF8, #8B5CF6); color: white; cursor: pointer;
                    box-shadow: 0 12px 32px rgba(56, 189, 248, .24); font-size: 0.98rem; font-weight: 700; transition: transform .2s ease, box-shadow .2s ease;
                }
                .cta:hover { transform: translateY(-3px); box-shadow: 0 18px 42px rgba(139, 92, 246, .38); }
                .cta:focus-visible { outline: 3px solid #F8FAFC; outline-offset: 4px; }
                @media (max-width: 640px) { #hero { min-height: 540px; } .hero-content { padding: 1.5rem; } }
            </style>
        </head>
        <body>
            <section id="hero" aria-label="Portfolio introduction">
                <canvas id="webgl-canvas"></canvas>
                <div class="hero-content">
                    <p class="eyebrow">Portfolio</p>
                    <h1>Muhammad Kashif Ansari</h1>
                    <p class="title">AI Engineer | Computer Vision Specialist | Data Scientist</p>
                    <p class="tagline">I am a Data Scientist, AI/ML Engineer, and Computer Vision Engineer passionate about turning data and intelligent technologies into practical, impactful solutions. My experience combines machine learning, deep learning, computer vision, data analysis, and software development. I have worked on projects including a deep-learning-based polyp detection system using CNNs, TensorFlow, OpenCV, and fuzzy logic, as well as data-driven applications such as Stockifistic. My academic and professional journey, along with my experience as a Computer Science Lab Instructor, has strengthened both my technical expertise and problem-solving abilities.
                                </p><p>I am continuously learning and exploring modern AI technologies, including RAG, LLMs, AI engineering, model optimization, and deployment. Moving forward, my goal is to grow as an AI/ML professional by solving challenging real-world problems, contributing to meaningful research, and building intelligent systems that create measurable impact. I am driven by curiosity, continuous learning, and a passion for transforming innovative ideas into reliable, real-world AI solutions.
                            </p>
                    <button class="cta" type="button" onclick="goToProjects()">Explore Work <span aria-hidden="true">↓</span></button>
                </div>
            </section>
            <script src="https://cdn.jsdelivr.net/npm/three@0.160.1/build/three.min.js"></script>
            <script>
                function goToProjects() {
                    // Add id="projects" to the future projects section in the Streamlit page.
                    window.parent.location.hash = "projects";
                }

                const canvas = document.getElementById("webgl-canvas");
                const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
                renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

                const scene = new THREE.Scene();
                const camera = new THREE.PerspectiveCamera(42, 1, 0.1, 100);
                camera.position.set(0, 0, 7.6);

                const group = new THREE.Group();
                scene.add(group);
                const geometry = new THREE.IcosahedronGeometry(2.25, 2);
                const wireframe = new THREE.LineSegments(
                    new THREE.WireframeGeometry(geometry),
                    new THREE.LineBasicMaterial({ color: 0x6dcbff, transparent: true, opacity: 0.53 })
                );
                group.add(wireframe);

                const particlesGeometry = new THREE.BufferGeometry();
                const particleCount = 280;
                const positions = new Float32Array(particleCount * 3);
                for (let i = 0; i < positions.length; i += 3) {
                    const radius = 3.3 + Math.random() * 3.4;
                    const theta = Math.random() * Math.PI * 2;
                    const phi = Math.acos(2 * Math.random() - 1);
                    positions[i] = radius * Math.sin(phi) * Math.cos(theta);
                    positions[i + 1] = radius * Math.cos(phi);
                    positions[i + 2] = radius * Math.sin(phi) * Math.sin(theta);
                }
                particlesGeometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));
                const particles = new THREE.Points(particlesGeometry, new THREE.PointsMaterial({ color: 0xa78bfa, size: 0.028, transparent: true, opacity: 0.75 }));
                scene.add(particles);

                let pointerX = 0, pointerY = 0;
                window.addEventListener("pointermove", (event) => {
                    pointerX = (event.clientX / window.innerWidth - 0.5) * 2;
                    pointerY = (event.clientY / window.innerHeight - 0.5) * 2;
                });
                function resize() {
                    const { width, height } = canvas.parentElement.getBoundingClientRect();
                    renderer.setSize(width, height, false);
                    camera.aspect = width / height;
                    camera.updateProjectionMatrix();
                }
                window.addEventListener("resize", resize);
                resize();

                function animate(time) {
                    requestAnimationFrame(animate);
                    group.rotation.y += 0.0025;
                    group.rotation.x += 0.0015;
                    particles.rotation.y = time * 0.00004;
                    group.rotation.y += pointerX * 0.0015;
                    group.rotation.x += pointerY * 0.001;
                    renderer.render(scene, camera);
                }
                animate(0);
            </script>
        </body>
        </html>
        """,
        height=720,
        scrolling=False,
    )


PROJECT_CATEGORIES = [
    "All Work",
    "Environment Art / CV",
    "Project Visualization",
    "Motion Graphics / AI",
    "Personal Projects",
]


def _safe_image(image_path: str) -> str:
    """Return a card-ready image URL, with a neutral fallback for empty values."""
    return image_path or "https://placehold.co/800x520/151A23/94A3B8?text=Project+Preview"


def _render_project_card(project: dict, index: int) -> None:
    """Render one visual project card and its stateful detail action."""
    title = escape(project.get("title", "Untitled Project"))
    category = escape(project.get("category", "Personal Projects"))
    image = escape(_safe_image(project.get("image", "")), quote=True)
    st.markdown(
        f"""
        <article class="project-card">
            <img class="project-card-image" src="{image}" alt="{title} project preview" />
            <div class="project-card-body">
                <span class="project-category">{category}</span>
                <h3>{title}</h3>
            </div>
        </article>
        """,
        unsafe_allow_html=True,
    )
    if st.button("View Project Details", key=f"view-project-{index}", use_container_width=True):
        st.session_state.selected_project_index = index
        st.session_state.work_view = "detail"
        st.rerun()


def render_project_detail(project: dict) -> None:
    """Render the selected project's reusable full-detail template."""
    if st.button("← Back to All Work", key="back-to-project-grid"):
        st.session_state.work_view = "grid"
        st.session_state.selected_project_index = None
        st.rerun()

    title = project.get("title", "Untitled Project")
    year = project.get("year", "YYYY")
    role = project.get("role", "AI Engineer")
    category = project.get("category", "Personal Projects")
    tools = project.get("tools", [])
    badges = "".join(f'<span class="skill-pill">{escape(str(tool))}</span>' for tool in tools)

    st.markdown(f"<h1 class='project-detail-title'>{escape(title)}</h1>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="project-meta">
            <span>{escape(str(year))}</span>
            <span>{escape(str(role))}</span>
            <span>{escape(str(category))}</span>
        </div>
        <p class="tool-label">Software used</p>
        <div class="tool-list">{badges}</div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("## Project Overview")
    st.write(project.get("overview", "Add a concise project overview."))

    st.markdown("## Concept & Reference")
    st.write(project.get("concept_reference", "Add visual references, mood boards, or architecture notes."))
    concept_images = project.get("concept_images", [])
    if concept_images:
        concept_columns = st.columns(min(3, len(concept_images)))
        for column, image in zip(concept_columns, concept_images):
            column.image(image, use_container_width=True)
    else:
        st.info("Add paths or URLs to `concept_images` in PORTFOLIO_DATA to show mood boards or diagrams.")

    st.markdown("## Work in Progress / Implementation Showcase")
    st.write(project.get("process_notes", "Add implementation notes and WIP milestones."))
    wip_images = project.get("wip_images", [])
    if wip_images:
        wip_columns = st.columns(min(3, len(wip_images)))
        for column, image in zip(wip_columns, wip_images):
            column.image(image, use_container_width=True)
    else:
        st.info("Add paths or URLs to `wip_images` in PORTFOLIO_DATA to show implementation progress.")


def render_work_section() -> None:
    """Render a filterable project grid or a selected project detail view."""
    st.session_state.setdefault("work_view", "grid")
    st.session_state.setdefault("selected_project_index", None)

    projects = PORTFOLIO_DATA["projects"]
    selected_index = st.session_state.selected_project_index
    if st.session_state.work_view == "detail" and isinstance(selected_index, int) and selected_index < len(projects):
        render_project_detail(projects[selected_index])
        return

    st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
    st.markdown("## Selected Work")
    current_category = st.session_state.get("project_category", "All Work")
    filter_columns = st.columns(len(PROJECT_CATEGORIES))
    for column, category in zip(filter_columns, PROJECT_CATEGORIES):
        if column.button(
            category,
            key=f"filter-{category}",
            type="primary" if category == current_category else "secondary",
            use_container_width=True,
        ):
            st.session_state.project_category = category
            st.rerun()

    active_category = st.session_state.get("project_category", "All Work")
    visible_projects = [
        (index, project)
        for index, project in enumerate(projects)
        if active_category == "All Work" or project.get("category") == active_category
    ]
    if not visible_projects:
        st.caption(f"No projects added to {active_category} yet.")
        return

    for start in range(0, len(visible_projects), 3):
        for column, (index, project) in zip(st.columns(3), visible_projects[start : start + 3]):
            with column:
                _render_project_card(project, index)


def _image_source(image_path: str) -> str:
    """Embed local images for HTML cards, or preserve remote image URLs."""
    if image_path.startswith(("https://", "http://", "data:")):
        return image_path
    image_file = Path(image_path)
    if image_file.is_file():
        mime_type = guess_type(image_file.name)[0] or "image/jpeg"
        return f"data:{mime_type};base64,{b64encode(image_file.read_bytes()).decode()}"
    return "https://placehold.co/800x620/151A23/94A3B8?text=Certificate"


def render_certificate_gallery() -> None:
    """Render a responsive certificate gallery with zoom-on-hover cards."""
    st.markdown("## Certificates & Credentials")
    certificates = PORTFOLIO_DATA["certificates"]
    for start in range(0, len(certificates), 3):
        for column, certificate in zip(st.columns(3), certificates[start : start + 3]):
            title = escape(certificate.get("title", "Certificate"))
            source = escape(_image_source(certificate.get("image", "")), quote=True)
            with column:
                st.markdown(
                    f'<div class="certificate-card"><img src="{source}" alt="{title}" /><span>{title}</span></div>',
                    unsafe_allow_html=True,
                )


def render_about_section() -> None:
    """Render a two-column professional bio, process, and availability section."""
    st.markdown("## About Me")
    identity = PORTFOLIO_DATA["identity"]
    left_column, right_column = st.columns([1, 1.45], gap="large")
    with left_column:
        profile_source = escape(_image_source(identity.get("profile_image", "")), quote=True)
        st.markdown(
            f'<div class="profile-frame"><img src="{profile_source}" alt="{escape(identity.get("name", "Profile photo"))}" /></div>',
            unsafe_allow_html=True,
        )
    with right_column:
        st.markdown(f"### {escape(identity.get('name', 'YOUR NAME'))}")
        st.write(identity.get("bio", identity.get("summary", "Add your story here.")))
        st.markdown("#### Software Proficiency")
        proficiency = [("Python", 92), ("Computer Vision", 88), ("Machine Learning", 85), ("Streamlit / Data Apps", 82)]
        for label, value in proficiency:
            st.markdown(
                f'<div class="proficiency-row"><div class="proficiency-label"><span>{label}</span><span>{value}%</span></div><div class="proficiency-track"><div class="proficiency-fill" style="width:{value}%"></div></div></div>',
                unsafe_allow_html=True,
            )
        st.markdown("#### Development Process")
        st.markdown(" ".join(f'<span class="skill-pill">{escape(step)}</span>' for step in identity.get("development_process", [])), unsafe_allow_html=True)
        st.markdown("#### Currently Learning / Exploring")
        st.markdown(" ".join(f'<span class="skill-pill">{escape(topic)}</span>' for topic in identity.get("currently_learning", [])), unsafe_allow_html=True)
        st.markdown("#### Available For")
        st.markdown('<div class="availability-list">' + "".join(f'<span class="availability-badge">{item}</span>' for item in ["Remote", "Freelance", "Full-time", "Collaborations"]) + "</div>", unsafe_allow_html=True)


def render_contact_footer() -> None:
    """Render direct contact, social links, resume download, and a compact footer."""
    contact = PORTFOLIO_DATA["contact"]
    email = contact.get("email", "your.email@example.com")
    status = contact.get("commission_status", "Available")
    social_links = [("in", "LinkedIn", contact.get("linkedin")), ("⌘", "GitHub", contact.get("github")), ("◉", "WhatsApp", contact.get("whatsapp")), ("◌", "Discord", contact.get("discord"))]
    links_html = "".join(f'<a class="social-button" href="{escape(str(url), quote=True)}" target="_blank" rel="noopener noreferrer">{icon} {label}</a>' for icon, label, url in social_links if url)
    st.markdown(
        f'<section class="contact-panel"><h2>Let\'s build something meaningful.</h2><p>For project inquiries, reach me directly at <a href="mailto:{escape(email)}">{escape(email)}</a>.</p><div class="status-open">🟢 {escape(status)}</div><div>{links_html}</div></section>',
        unsafe_allow_html=True,
    )
    resume_file = Path(contact.get("resume_path", ""))
    if resume_file.is_file():
        st.download_button("Download Resume (PDF)", data=resume_file.read_bytes(), file_name=resume_file.name, mime="application/pdf", use_container_width=True)
    else:
        st.download_button("Download Resume (PDF)", data=b"", file_name="resume.pdf", mime="application/pdf", disabled=True, use_container_width=True, help="Add your PDF at the resume_path set in PORTFOLIO_DATA.")
    st.markdown(f'<footer class="site-footer">© 2026 {escape(PORTFOLIO_DATA["identity"].get("name", "YOUR NAME"))}. </footer>', unsafe_allow_html=True)


def _portfolio_text_chunks() -> list[str]:
    """Convert the editable portfolio dictionary into retrieval-friendly chunks."""
    portfolio_text = json.dumps(PORTFOLIO_DATA, indent=2, ensure_ascii=False)
    try:
        from langchain_text_splitters import RecursiveCharacterTextSplitter

        splitter = RecursiveCharacterTextSplitter(chunk_size=450, chunk_overlap=75)
        return splitter.split_text(portfolio_text)
    except ImportError:
        return [portfolio_text[start : start + 450] for start in range(0, len(portfolio_text), 375)]


@st.cache_resource(show_spinner="Preparing portfolio knowledge base…")
def setup_rag_chatbot():
    """Create and cache a local FAISS vector store from PORTFOLIO_DATA."""
    try:
        from langchain_community.embeddings import HuggingFaceEmbeddings
        from langchain_community.vectorstores import FAISS

        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )
        vector_store = FAISS.from_texts(_portfolio_text_chunks(), embedding=embeddings)
        return vector_store, None
    except Exception as error:
        return None, f"Portfolio search is unavailable: {error}"


def _retrieve_portfolio_context(vector_store, question: str) -> str:
    """Retrieve the four most relevant portfolio chunks for a visitor question."""
    documents = vector_store.similarity_search(question, k=4)
    return "\n\n---\n\n".join(document.page_content for document in documents)


def render_chatbot_ui() -> None:
    """Render the expandable, retrieval-grounded Groq portfolio assistant."""
    name = PORTFOLIO_DATA["identity"].get("name", "YOUR NAME")
    vector_store, index_error = setup_rag_chatbot()

    with st.expander("✦ Ask my portfolio assistant", expanded=False):
        st.caption("Ask about experience, skills, education, or portfolio projects.")
        if index_error:
            st.warning(index_error)
            return

        api_key = st.secrets.get("GROQ_API_KEY", None)
        if not api_key:
            st.warning("Portfolio chat is ready to use once `GROQ_API_KEY` is added to Streamlit secrets.")
            st.code('GROQ_API_KEY = "gsk_..."', language="toml")
            return

        history_key = "portfolio_chat_messages"
        st.session_state.setdefault(history_key, [])
        for message in st.session_state[history_key]:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        question = st.chat_input("Ask about my work, skills, or experience…", key="portfolio-chat-input")
        if not question:
            return

        st.session_state[history_key].append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            try:
                from langchain_core.messages import HumanMessage, SystemMessage
                from langchain_groq import ChatGroq

                context = _retrieve_portfolio_context(vector_store, question)
                system_prompt = f"""You are the AI assistant for {name}'s portfolio.
Answer questions concisely using ONLY the retrieved context. Do not infer, invent,
or supplement details not present in the context. If the query is off-topic or
unrelated to {name}'s experience, skills, projects, or education, politely respond
exactly: 'I am specialized to answer questions regarding {name}'s portfolio, experience,
and projects. Please feel free to ask about their work!'

Retrieved context:
{context}"""
                model = ChatGroq(
                    model="llama-3.1-8b-instant",
                    api_key=api_key,
                    temperature=0,
                    max_tokens=350,
                )
                response = model.invoke([SystemMessage(content=system_prompt), HumanMessage(content=question)])
                answer = response.content if isinstance(response.content, str) else str(response.content)
            except Exception:
                answer = "I couldn't reach the portfolio assistant right now. Please try again in a moment."

            st.markdown(answer)
        st.session_state[history_key].append({"role": "assistant", "content": answer})


st.set_page_config(
    page_title="Kashif | Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)
inject_custom_css()
render_hero_section()
render_work_section()
render_certificate_gallery()
render_about_section()
render_contact_footer()
render_chatbot_ui()

# Page sections, FAISS retrieval, and Groq chatbot logic will be added next.
