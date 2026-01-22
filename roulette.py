import tkinter as tk
import math
import random
import time

class RouletteWidget:
    def __init__(self, parent, seed_hex):
        self.parent = parent
        self.seed_hex = seed_hex
        self.frame = tk.Frame(parent, bg='#1a1a2e')
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.roulette_numbers = [
            0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10,
            5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26
        ]
        
        self.is_spinning = False
        self.current_rotation = 0
        self.result = None
        self.history = []
        
        self._create_ui()
    
    def _get_color(self, num):
        if num == 0:
            return '#059669'  # Vert
        reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        return '#dc2626' if num in reds else '#1f2937'
    
    def _hash_seed(self, nonce):
        combined = self.seed_hex + str(nonce)
        hash_val = 0
        for char in combined:
            hash_val = ((hash_val << 5) - hash_val) + ord(char)
            hash_val = hash_val & 0xFFFFFFFF
        return abs(hash_val)
    
    def _create_ui(self):
        title = tk.Label(
            self.frame,
            text="🎰 ROULETTE CASINO 🎰",
            font=("Arial", 32, "bold"),
            bg='#1a1a2e',
            fg='#ffd700'
        )
        title.pack(pady=20)
        
        self.canvas = tk.Canvas(
            self.frame,
            width=500,
            height=500,
            bg='#1a1a2e',
            highlightthickness=0
        )
        self.canvas.pack(pady=20)
        
        self._draw_roulette()
        
        self.spin_button = tk.Button(
            self.frame,
            text="🎲 LANCER LA ROULETTE",
            font=("Arial", 18, "bold"),
            bg='#ffd700',
            fg='#1a1a2e',
            activebackground='#ffed4e',
            command=self.spin,
            cursor="hand2",
            padx=20,
            pady=10
        )
        self.spin_button.pack(pady=20)
        
        self.result_label = tk.Label(
            self.frame,
            text="",
            font=("Arial", 48, "bold"),
            bg='#1a1a2e',
            fg='white'
        )
        self.result_label.pack(pady=10)
        
        history_frame = tk.Frame(self.frame, bg='#2a2a4e')
        history_frame.pack(pady=20, padx=20, fill=tk.X)
        
        tk.Label(
            history_frame,
            text="📊 Historique",
            font=("Arial", 16, "bold"),
            bg='#2a2a4e',
            fg='white'
        ).pack(pady=5)
        
        self.history_frame = tk.Frame(history_frame, bg='#2a2a4e')
        self.history_frame.pack(pady=5)
    
    def _draw_roulette(self):
        self.canvas.delete("all")
        
        cx, cy = 250, 250
        radius = 200
        
        segment_angle = 360 / 37
        for i, num in enumerate(self.roulette_numbers):
            start_angle = i * segment_angle + self.current_rotation
            color = self._get_color(num)
            
            self.canvas.create_arc(
                cx - radius, cy - radius, cx + radius, cy + radius,
                start=start_angle, extent=segment_angle,
                fill=color, outline='#ffd700', width=2
            )
            
            angle_rad = math.radians(start_angle + segment_angle / 2)
            text_radius = radius - 30
            tx = cx + text_radius * math.cos(angle_rad)
            ty = cy - text_radius * math.sin(angle_rad)
            
            self.canvas.create_text(
                tx, ty, text=str(num),
                fill='white', font=("Arial", 12, "bold")
            )
        
        self.canvas.create_oval(
            cx - 30, cy - 30, cx + 30, cy + 30,
            fill='#ffd700', outline='#ffed4e', width=3
        )
        
        self.canvas.create_polygon(
            cx, cy - radius - 20,
            cx - 15, cy - radius,
            cx + 15, cy - radius,
            fill='#ffd700', outline='black', width=2
        )
    
    def spin(self):
        if self.is_spinning:
            return
        
        self.is_spinning = True
        self.spin_button.config(state=tk.DISABLED, text="🎰 EN COURS...")
        self.result_label.config(text="")
        
        nonce = int(time.time() * 1000)
        hash_val = self._hash_seed(nonce)
        winning_number = hash_val % 37
        target_index = self.roulette_numbers.index(winning_number)
        segment_angle = 360 / 37
        spins = random.uniform(5, 8)
        target_rotation = -(spins * 360 + target_index * segment_angle - 90)
        
        self._animate_spin(target_rotation, winning_number, 0)
    
    def _animate_spin(self, target, winning_number, step):
        if step < 100:
            progress = step / 100
            eased_progress = 1 - math.pow(1 - progress, 3)
            self.current_rotation = eased_progress * target
            
            self._draw_roulette()
            self.parent.after(40, lambda: self._animate_spin(target, winning_number, step + 1))
        else:
            self.current_rotation = target
            self._draw_roulette()
            
            normalized_rotation = self.current_rotation % 360
            segment_angle = 360 / 37
            pointer_angle = (90 - normalized_rotation) % 360
            segment_index = int(pointer_angle / segment_angle) % 37
            actual_number = self.roulette_numbers[segment_index]
            
            self.is_spinning = False
            self.result = actual_number
            self.history.insert(0, actual_number)
            self.history = self.history[:10]
            
            color = self._get_color(actual_number)
            self.result_label.config(
                text=str(actual_number),
                fg=color
            )
            
            self._update_history()
            
            self.spin_button.config(state=tk.NORMAL, text="🎲 LANCER LA ROULETTE")
    
    def _update_history(self):
        for widget in self.history_frame.winfo_children():
            widget.destroy()
        
        for num in self.history:
            color = self._get_color(num)
            label = tk.Label(
                self.history_frame,
                text=str(num),
                font=("Arial", 14, "bold"),
                bg=color,
                fg='white',
                width=3,
                height=1
            )
            label.pack(side=tk.LEFT, padx=2)


def create_roulette(seed_hex):
    root = tk.Tk()
    root.title("Roulette Casino")
    root.geometry("600x800")
    root.configure(bg='#1a1a2e')
    
    roulette = RouletteWidget(root, seed_hex)
    
    root.mainloop()

