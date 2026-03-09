from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def create_receipt(name, amount, payment_method="Cash", receipt_id="REC-001"):
    filename = f"receipt_{receipt_id}.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width/2, height-80, "PAYMENT RECEIPT")

    c.setFont("Helvetica", 12)
    y = height - 140
    c.drawString(60, y, f"Receipt #: {receipt_id}")
    y -= 20
    c.drawString(60, y, f"Date: {datetime.now()}")
    y -= 40
    c.drawString(60, y, f"Received from: {name}")
    y -= 30
    c.drawString(60, y, f"Amount: PKR {amount:,.2f}")
    y -= 25
    c.drawString(60, y, f"Payment method: {payment_method}")
    y -= 50
    c.setFont("Helvetica-Bold", 14)
    c.drawString(60, y, f"Total Paid: PKR {amount:,.2f}")
    
    c.showPage()
    c.save()
    print(f"Receipt saved → {filename}")

# use of this function is in GUI.
def generate():
    name = entry_name.get()
    try:
        amt = float(entry_amount.get())
    except:
        messagebox.showerror("Error", "Amount must be a number")
        return
    
    method = entry_method.get() or "Cash"
    rid = entry_id.get() or f"REC-{datetime.now().strftime('%Y%m%d%H%M')}"
    
    create_receipt(name, amt, method, rid)
    messagebox.showinfo("Done", "Receipt PDF created!")

root = tk.Tk()
root.title("Payment Receipt Generator")
root.geometry("420x380")

tk.Label(root, text="Customer Name:").pack(pady=8)
entry_name = tk.Entry(root, width=35); entry_name.pack()

tk.Label(root, text="Amount (PKR):").pack(pady=8)
entry_amount = tk.Entry(root, width=35); entry_amount.pack()

tk.Label(root, text="Payment Method:").pack(pady=8)
entry_method = tk.Entry(root, width=35); entry_method.pack()

tk.Label(root, text="Receipt ID (optional):").pack(pady=8)
entry_id = tk.Entry(root, width=35); entry_id.pack()

tk.Button(root, text="Generate Receipt PDF", command=generate, bg="#AF4C95", fg="white", padx=20, pady=10).pack(pady=30)

root.mainloop()