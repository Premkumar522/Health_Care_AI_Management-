def get_response(user_input):

    user_input = user_input.lower()

    if "diabetes" in user_input:
        return """
Diabetes is a condition where blood sugar levels are high.

Recommendations:
• Maintain healthy diet
• Exercise regularly
• Monitor blood sugar
• Consult Endocrinologist
"""

    elif "heart" in user_input:
        return """
Heart Disease Tips:

• Reduce cholesterol
• Monitor blood pressure
• Regular exercise
• Consult Cardiologist
"""

    elif "kidney" in user_input:
        return """
Kidney Disease Tips:

• Drink enough water
• Monitor BP
• Reduce salt intake
• Consult Nephrologist
"""

    elif "appointment" in user_input:
        return """
To book appointment:

1. Select Doctor
2. Choose Available Slot
3. Confirm Booking
"""

    elif "hello" in user_input:
        return "Hello 👋 How can I assist you today?"

    else:
        return """
I'm Healthcare AI Assistant.

You can ask about:
• Diabetes
• Heart Disease
• Kidney Disease
• Appointments
• Health Tips
"""