import tkinter as tk
from dotenv import load_dotenv
import os
import openai


load_dotenv()
key = os.getenv("OPENAI_API_KEY")


client = openai.OpenAI(api_key=key)


def get_completion():
    prompt = entry.get()
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[{"role": "user", "content": prompt}]
    )
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, response.choices[0].message.content)


root = tk.Tk()
root.title("AI Completion GUI")

tk.Label(root, text="Enter your prompt:").pack()

entry = tk.Entry(root, width=50)
entry.pack()

tk.Button(root, text="Submit", command=get_completion).pack()

output_box = tk.Text(root, height=10, width=60)
output_box.pack()

root.mainloop()


