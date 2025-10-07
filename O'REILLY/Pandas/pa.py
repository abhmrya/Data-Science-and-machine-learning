import pandas as pd
from io import StringIO

data = """Query,Intent,Disease,Answer
What are the benefits of drinking water?,basic_health_query,N/A,Staying hydrated is crucial for a healthy body. Drinking enough water helps with nutrient absorption, waste removal, and regulating body temperature.
How much water should I drink daily?,basic_health_query,N/A,The general recommendation is about 8 glasses (around 2 liters) per day, but it can vary based on your activity level, climate, and overall health.
What are some tips for a healthy diet?,basic_health_query,N/A,For a healthy diet, focus on eating a variety of fruits, vegetables, whole grains, lean proteins, and healthy fats. Try to limit processed foods, sugary drinks, and unhealthy fats.
How can I improve my sleep?,basic_health_query,N/A,To improve your sleep, try to maintain a regular sleep schedule, create a relaxing bedtime routine, avoid caffeine and large meals before bed, and ensure your bedroom is dark and quiet.
What is a fever?,basic_health_query,N/A,A fever is when your body temperature is higher than normal. It's often a sign that your body is fighting off an infection or illness.
What is the normal body temperature?,basic_health_query,N/A,The average normal body temperature is around 98.6°F (37°C), but it can vary slightly from person to person and throughout the day.
How to measure body temperature?,basic_health_query,N/A,You can measure body temperature using a digital thermometer placed under the tongue, in the ear, or on the forehead.
When should I see a doctor?,basic_health_query,N/A,You should see a doctor for persistent or severe symptoms, a high fever, a sudden change in your health, or any new or unusual health concerns.
What is a doctor?,basic_health_query,N/A,A doctor is a medical professional who is licensed to practice medicine. They diagnose and treat illnesses and injuries.
What is a virus?,basic_health_query,N/A,A virus is a microscopic infectious agent that can only replicate inside the living cells of other organisms.
What is a bacterium?,basic_health_query,N/A,A bacterium is a single-celled microorganism that can live in various environments. While some cause diseases, many are harmless and even beneficial to your body.
What is an antibiotic?,basic_health_query,N/A,An antibiotic is a type of medication that fights bacterial infections. It is important to remember that antibiotics are not effective against viruses.
What is a vaccine?,basic_health_query,N/A,A vaccine is a substance used to stimulate the production of antibodies and provide immunity against one or several diseases.
How can I avoid getting sick?,basic_health_query,N/A,To avoid getting sick, wash your hands frequently with soap and water, avoid touching your face, and get enough rest.
What is the flu?,basic_health_query,N/A,The flu (influenza) is a contagious respiratory illness caused by influenza viruses. Symptoms are generally more severe than a common cold.
What is a balanced diet?,basic_health_query,N/A,A balanced diet includes all the major food groups in the right proportions to provide your body with the necessary nutrients for good health.
What are some good sources of protein?,basic_health_query,N/A,Good sources of protein include lean meats, poultry, fish, eggs, dairy products, legumes, nuts, and seeds.
How can I manage stress?,basic_health_query,N/A,Managing stress can involve exercise, meditation, deep breathing, spending time in nature, or engaging in a hobby you enjoy.
What is an allergy?,basic_health_query,N/A,An allergy is an overreaction of your body's immune system to a harmless substance, like pollen or certain foods.
What is a migraine?,basic_health_query,N/A,A migraine is a type of severe headache that can be accompanied by symptoms like throbbing pain, sensitivity to light and sound, and nausea.
What are some healthy habits to start?,basic_health_query,N/A,Some healthy habits to start include exercising regularly, eating a balanced diet, getting enough sleep, and managing your stress.
What is body mass index (BMI)?,basic_health_query,N/A,BMI is a measure of body fat based on your height and weight. It can be a useful screening tool but does not diagnose body fatness or health.
How do I stop a nosebleed?,basic_health_query,N/A,To stop a nosebleed, sit or stand, lean forward slightly, and pinch the soft part of your nose just below the bony ridge for 10-15 minutes.
What should I do if I get a cut?,basic_health_query,N/A,For a minor cut, wash the area with soap and water, apply pressure with a clean cloth, and cover it with a bandage.
What is a calorie?,basic_health_query,N/A,A calorie is a unit of energy in food. Your body needs calories for energy to function, but consuming too many can lead to weight gain.
"""
df = pd.read_csv(StringIO(data))
print(df.head())
df.to_csv("pyy.excel")