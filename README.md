## Flask Application Design for Language Learning Website

### HTML Files

- **index.html:** Main page of the website, providing an overview of the website and its features.
- **lessons.html:** Page that lists all the Telugu lessons available on the website.
- **lesson.html:** Page that displays a specific Telugu lesson, including grammar explanations, vocabulary lists, and exercises.
- **exercises.html:** Page that contains interactive exercises to practice the Telugu language skills learned in the lessons.

### Routes

- **@app.route('/')**: Main route that displays the `index.html` page.
- **@app.route('/lessons')**: Route that displays the `lessons.html` page.
- **@app.route('/lesson/<lesson_id>')**: Route that displays a specific Telugu lesson based on the `lesson_id` in the `lesson.html` page.
- **@app.route('/exercises')**: Route that displays the `exercises.html` page.
- **@app.route('/submit_exercise', methods=['POST'])**: Route that handles the submission of exercises and provides feedback to the user.