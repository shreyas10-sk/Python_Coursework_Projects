<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shreyas Kanagal | Economics & Data Analytics</title>
    <style>
        :root {
            --primary: #0039A6; /* UT Dallas blue */
            --secondary: #EFDF00; /* Complimentary gold */
            --dark: #1A1A1A;
            --light: #F8F9FA;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: var(--dark);
            background-color: var(--light);
        }
        .container {
            max-width: 1100px;
            margin: 0 auto;
            padding: 0 20px;
        }
        header {
            background: linear-gradient(135deg, var(--primary) 0%, #002366 100%);
            color: white;
            padding: 60px 0 40px;
            text-align: center;
            margin-bottom: 40px;
            position: relative;
            overflow: hidden;
        }
        header::after {
            content: "";
            position: absolute;
            bottom: -50px;
            left: 0;
            right: 0;
            height: 100px;
            background: var(--light);
            transform: skewY(-2deg);
            z-index: 1;
        }
        h1 {
            margin: 0;
            font-size: 2.8em;
            position: relative;
            z-index: 2;
        }
        .tagline {
            font-size: 1.2em;
            opacity: 0.9;
            position: relative;
            z-index: 2;
        }
        h2 {
            color: var(--primary);
            border-bottom: 2px solid var(--secondary);
            padding-bottom: 8px;
            margin-top: 0;
        }
        .card {
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            margin-bottom: 30px;
            transition: transform 0.3s ease;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin-top: 15px;
        }
        .skill {
            background-color: #E6EFFF;
            padding: 8px 18px;
            border-radius: 20px;
            font-size: 0.9em;
            transition: all 0.3s ease;
        }
        .skill:hover {
            background-color: var(--primary);
            color: white;
            transform: scale(1.05);
        }
        .sports-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        .sport {
            background-color: #F5F5F5;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
        }
        .sport-icon {
            font-size: 2em;
            margin-bottom: 10px;
            color: var(--primary);
        }
        footer {
            text-align: center;
            padding: 30px;
            background-color: var(--dark);
            color: white;
            margin-top: 50px;
        }
        .contact a {
            color: var(--secondary);
            text-decoration: none;
            font-weight: 600;
        }
        .contact a:hover {
            text-decoration: underline;
        }
        .profile-img {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid white;
            margin: 0 auto 20px;
            display: block;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }
        @media (max-width: 768px) {
            h1 {
                font-size: 2.2em;
            }
            .card {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <!-- Replace with your actual image path -->
            <img src="profile.jpg" alt="Shreyas Kanagal" class="profile-img">
            <h1>Shreyas Kanagal</h1>
            <p class="tagline">Economics | Quantitative Analytics | Data Science</p>
        </div>
    </header>

    <div class="container">
        <section class="card">
            <h2>About Me</h2>
            <p>I'm a passionate junior at The University of Texas at Dallas pursuing a Bachelor's degree in Economics with a minor in Business Intelligence and Analytics. My academic journey focuses on bridging economic theory with data-driven decision making.</p>
            <p>With a strong quantitative foundation, I'm preparing for a career in financial analytics where I can apply statistical modeling and machine learning to solve complex market problems. I'm particularly interested in algorithmic trading strategies and risk assessment models.</p>
            <p>When I'm not analyzing datasets or studying economic trends, you'll find me in the gym, on the basketball court, or competing in table tennis tournaments. I believe the discipline of athletics complements the rigor of quantitative analysis.</p>
        </section>

        <section class="card">
            <h2>Academic Focus</h2>
            <h3>University of Texas at Dallas</h3>
            <p><strong>BS in Economics</strong> | Minor in Business Intelligence and Analytics | GPA: 3.8</p>
            <p><strong>Expected Graduation:</strong> May 2025</p>
            
            <h3 style="margin-top: 25px;">Core Competencies</h3>
            <div class="skills">
                <span class="skill">Econometrics</span>
                <span class="skill">Statistical Modeling</span>
                <span class="skill">Financial Analysis</span>
                <span class="skill">Python</span>
                <span class="skill">R Programming</span>
                <span class="skill">SQL</span>
                <span class="skill">Tableau</span>
                <span class="skill">Machine Learning</span>
                <span class="skill">Data Visualization</span>
                <span class="skill">Stata</span>
                <span class="skill">Excel VBA</span>
            </div>
        </section>

        <section class="card">
            <h2>Athletic Pursuits</h2>
            <div class="sports-grid">
                <div class="sport">
                    <div class="sport-icon">🏊</div>
                    <h3>Competitive Swimming</h3>
                    <p>15+ years experience, specializing in freestyle and butterfly events</p>
                </div>
                <div class="sport">
                    <div class="sport-icon">🏀</div>
                    <h3>Basketball</h3>
                    <p>Varsity player in high school, now recreational league competitor</p>
                </div>
                <div class="sport">
                    <div class="sport-icon">🎯</div>
                    <h3>Table Tennis</h3>
                    <p>Tournament-level player with competitive ranking</p>
                </div>
                <div class="sport">
                    <div class="sport-icon">💪</div>
                    <h3>Strength Training</h3>
                    <p>5-day/week regimen focused on athletic performance</p>
                </div>
            </div>
        </section>

        <section class="card">
            <h2>Career Aspirations</h2>
            <p>My goal is to work at the intersection of finance and technology, leveraging quantitative methods to:</p>
            <ul>
                <li>Develop predictive models for financial markets</li>
                <li>Create algorithmic trading strategies</li>
                <li>Optimize risk assessment frameworks</li>
                <li>Bridge economic theory with machine learning applications</li>
            </ul>
            <p>I'm particularly interested in roles that combine my analytical training with my passion for solving complex, real-world financial problems.</p>
        </section>
    </div>

    <footer>
        <div class="container contact">
            <h2>Connect With Me</h2>
            <p>Email: <a href="mailto:your.email@utdallas.edu">skanagal@utdallas.edu</a> | 
               LinkedIn: <a href="https://linkedin.com/in/shreyaskanagal" target="_blank">linkedin.com/in/shreyaskanagal</a> | 
               GitHub: <a href="https://github.com/shreyas-k" target="_blank">github.com/shreyas-k</a></p>
            <p>&copy; 2023 Shreyas Kanagal. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>