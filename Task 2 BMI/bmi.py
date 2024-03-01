import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import csv
from datetime import datetime

class BMI_Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")

        self.weight_label = tk.Label(root, text="Enter your Weight (kg):")
        self.weight_label.grid(row=0, column=0)

        self.weight_entry = tk.Entry(root)
        self.weight_entry.grid(row=0, column=1)

        self.height_label = tk.Label(root, text="Enter your Height (cm):")
        self.height_label.grid(row=1, column=0)

        self.height_entry = tk.Entry(root)
        self.height_entry.grid(row=1, column=1)

        self.calculate_button = tk.Button(root, text="Click to Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, columnspan=2)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get()) / 100  # Convert height from cm to meters

            bmi = weight / (height ** 2)
            bmi = round(bmi, 2)

            category = self.get_bmi_category(bmi)

            messagebox.showinfo("BMI Result", f"Your BMI is: {bmi}\nCategory: {category}")

            # Store data and visualize the result
            self.store_and_visualize_data(weight, height * 100, bmi, category)  # Convert height back to cm

        except ValueError:
            messagebox.showerror("Error", "Please enter valid weight and height.")

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal Weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

    def store_and_visualize_data(self, weight, height, bmi, category):
        # Store data in a CSV file
        with open('bmi_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), weight, height, bmi, category])

        # Visualize BMI trends
        dates = []
        bmis = []
        categories = []
        with open('bmi_data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                dates.append(row[0])
                bmis.append(float(row[3]))
                categories.append(row[3])

        plt.figure(figsize=(8, 6))
        plt.plot(dates, bmis, marker='o', label='BMI')
        plt.xlabel('Date')
        plt.ylabel('BMI')
        plt.title('BMI Trends Over Time')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()


def main():
    root = tk.Tk()
    app = BMI_Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
