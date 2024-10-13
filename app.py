from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data to mimic a database
posts = []

@app.route('/')
def home():
    return render_template('posts.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({'title': title, 'content': content})  # Add the new post to the list
        return redirect(url_for('thank_you'))  # Redirect after submission
    return render_template('create_post.html')  # Render post creation form

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        message = request.form['message']
        print(f"Name: {name}, Mobile: {mobile}, Message: {message}")  # Debugging output
        return redirect(url_for('thank_you'))  # Redirect to a thank-you page

    return render_template('contact.html')  # Render the contact form page

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')  # Render a thank-you page

@app.route('/post-history')
def post_history():
    return render_template('post_history.html', posts=posts)  # Render the post history page

if __name__ == '__main__':
    app.run(debug=True)







