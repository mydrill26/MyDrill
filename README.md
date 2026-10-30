MyDrill is a Python-based gymnastics drill recommendation application designed to help coaches quickly find suitable drills for gymnasts based on the apparatus, skill and specific problem they are experiencing.

The project was created from my experience as a gymnastics coach, where gymnasts can be working on the same skill but require different drills depending on their individual difficulties.

Features
  - Select an apparatus, skill and specific problem
  - Dependent dropdown menus that update based on previous selections
  - Drill recommendations retrieved from a CSV dataset
  - Displays two recommended drills
  - Shows the purpose, level and equipment required
  - Includes video demonstrations for selected drills
  - Simple graphical interface built using CustomTkinter

Technologies Used
  - Python 3
  - pandas
  - tkinter
  - CustomTkinter
  - subprocess
  - os
  - CSV data

How It Works

MyDrill uses a CSV dataset containing information about gymnastics drills. The user selects an apparatus, followed by a skill and a specific problem. The application uses pandas to filter the dataset and find the row that matches all three selections. The matching recommendation is then displayed in the interface, including the drills, purpose, level and equipment. Each recommendation can also contain two video filenames. The application uses these filenames to locate the correct videos inside the Gymnastics Videos folder and open them when the user selects the video buttons.

Development

During development, I began with a simple text-based recommendation system before developing the project into a graphical application.

The final version includes dependent dropdown menus, pandas filtering, dynamic recommendations and video demonstrations.

One of the main challenges was understanding how different parts of the program depend on each other, particularly variables, functions, interface elements and file paths. Developing MyDrill helped strengthen my understanding of Python, data handling and debugging.

