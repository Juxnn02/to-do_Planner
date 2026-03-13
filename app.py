from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store our tasks 
# (Since this is a simple midterm project, we won't use a database)
tasks = []
task_id_counter = 1

@app.route('/')
def home():
    # Renders the HTML template and passes the tasks list to it
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    global task_id_counter
    global tasks
    
    # Check if the request is a POST (the form was actually submitted)
    if request.method == 'POST':
        # Get the task content from the submitted form, default to empty string
        task_content = request.form.get('content', '')
        
        # Only add if the string is not empty
        if task_content and task_content.strip():
            tasks.append({
                'id': task_id_counter, 
                'content': task_content.strip()
            })
            task_id_counter += 1
            
    # Always redirect back to the home page, preventing crashes on refresh or manual navigation
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    # Rebuild the list, excluding the task with the matching ID
    tasks = [task for task in tasks if task['id'] != task_id]
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Required Configuration from the Midterm Assessment PDF
    app.run(debug=True, host="0.0.0.0", port=8080)