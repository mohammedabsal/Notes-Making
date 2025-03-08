import streamlit as st
import speech_recognition as sr
from datetime import datetime, timedelta
import json
from pathlib import Path

# --- Session State Initialization ---
if 'notes' not in st.session_state:
    st.session_state.notes = []
if 'todos' not in st.session_state:
    st.session_state.todos = []
if 'points' not in st.session_state:
    st.session_state.points = 0

def save_data():
    """Save all data to JSON files"""
    data = {
        'notes': st.session_state.notes,
        'todos': st.session_state.todos,
        'points': st.session_state.points
    }
    Path('data').mkdir(exist_ok=True)
    with open('data/app_data.json', 'w') as f:
        json.dump(data, f)

def load_data():
    """Load data from JSON files"""
    try:
        with open('data/app_data.json', 'r') as f:
            data = json.load(f)
            st.session_state.notes = data.get('notes', [])
            st.session_state.todos = data.get('todos', [])
            st.session_state.points = data.get('points', 0)
    except FileNotFoundError:
        pass

def voice_to_text():
    """Convert voice to text using speech recognition"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening... Speak now!")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            st.error("Could not understand audio")
            return None
        except sr.RequestError:
            st.error("Could not request results")
            return None

def parse_voice_command(text):
    """Parse voice command for tomorrow's todo"""
    if text and "for tomorrow" in text.lower():
        task = text.lower().replace("for tomorrow", "").strip()
        tomorrow = datetime.now() + timedelta(days=1)
        return {
            'task': task,
            'date': tomorrow.strftime('%Y-%m-%d'),
            'completed': False
        }
    return None

def award_points(points):
    """Award points for completing tasks"""
    st.session_state.points += points
    save_data()

# --- Main App UI ---
def main():
    st.title("📝 Smart Note Taking App")
    load_data()
    
    # Sidebar for points
    with st.sidebar:
        st.header("🏆 Achievement Points")
        st.write(f"Total Points: {st.session_state.points}")
        
        # Achievement badges
        if st.session_state.points >= 100:
            st.write("🌟 Note-Taking Pro")
        if st.session_state.points >= 50:
            st.write("📈 Productivity Master")
        if st.session_state.points >= 25:
            st.write("🎯 Goal Getter")

    # Main tabs
    tab1, tab2 = st.tabs(["📝 Notes", "✔️ ToDos"])

    # Notes Tab
    with tab1:
        st.header("Create New Note")
        note_type = st.radio("Input Type:", ["Text", "Voice"])
        
        if note_type == "Text":
            note_text = st.text_area("Write your note:")
            if st.button("Save Note"):
                if note_text:
                    st.session_state.notes.append({
                        'text': note_text,
                        'date': datetime.now().strftime('%Y-%m-%d %H:%M')
                    })
                    save_data()
                    award_points(5)  # Points for creating a note
                    st.success("Note saved!")
        else:
            if st.button("Start Voice Recording"):
                text = voice_to_text()
                if text:
                    st.write(f"Recorded: {text}")
                    todo = parse_voice_command(text)
                    if todo:
                        st.session_state.todos.append(todo)
                        award_points(10)  # Extra points for voice todo
                    else:
                        st.session_state.notes.append({
                            'text': text,
                            'date': datetime.now().strftime('%Y-%m-%d %H:%M')
                        })
                        award_points(8)  # Points for voice note
                    save_data()
                    st.success("Voice note saved!")

        # Display existing notes
        st.header("Your Notes")
        for note in reversed(st.session_state.notes):
            with st.expander(f"Note from {note['date']}"):
                st.write(note['text'])

    # ToDos Tab
    with tab2:
        st.header("ToDo List")
        new_todo = st.text_input("Add new todo:")
        if st.button("Add Todo"):
            if new_todo:
                st.session_state.todos.append({
                    'task': new_todo,
                    'date': datetime.now().strftime('%Y-%m-%d'),
                    'completed': False
                })
                save_data()
                award_points(5)  # Points for creating a todo

        # Display todos
        st.subheader("Today's Tasks")
        today = datetime.now().strftime('%Y-%m-%d')
        for i, todo in enumerate(st.session_state.todos):
            if todo['date'] == today:
                col1, col2 = st.columns([1, 4])
                with col1:
                    if st.checkbox("", todo['completed'], key=f"todo_{i}"):
                        st.session_state.todos[i]['completed'] = True
                        award_points(10)  # Points for completing a task
                        save_data()
                with col2:
                    st.write(todo['task'])

        st.subheader("Future Tasks")
        future_todos = [todo for todo in st.session_state.todos 
                       if todo['date'] > today]
        for i, todo in enumerate(future_todos):
            st.write(f"📅 {todo['date']}: {todo['task']}")

if __name__ == "__main__":
    main()