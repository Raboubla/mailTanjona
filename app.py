import tkinter as tk
from tkinter import ttk, messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr
import os
import re
from datetime import datetime

class EmailApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Application d'Envoi d'Emails")
        self.root.geometry("800x600")
        self.root.configure(bg="#0f172a")

        # Paramètres email
        self.email = "contact@crypto-invest-expert.com"
        self.password = "0Fx]7ZE4YwiT"
        self.smtp_server = "smtp.hostinger.com"
        self.smtp_port = 587

        # Chemins vers les templates HTML
        self.template_paths = {
            "mail1": "template1.txt",
            "mail2": "template2.txt",
            "mail3": "template3.txt",
            "mail4": "template4.txt"
        }

        # Initialisation de l'interface
        self.setup_ui()

    def setup_ui(self):
        # Style
        style = ttk.Style()
        style.theme_use('clam')  # Utiliser un thème qui permet de personnaliser les couleurs
        
        # Configuration des styles
        style.configure('TFrame', background='#1e293b')
        style.configure('TNotebook', background='#1e293b')
        style.configure('TNotebook.Tab', background='#2d3748', foreground='#ffffff', padding=[10, 5])
        style.map('TNotebook.Tab', background=[('selected', '#6366f1')])
        style.configure('TLabel', background='#1e293b', foreground='#ffffff', font=('Arial', 10))
        
        # Configurer les boutons avec des couleurs visibles
        style.configure('TButton', 
                        background='#4f46e5', 
                        foreground='#ffffff', 
                        font=('Arial', 10, 'bold'),
                        padding=6)
        style.map('TButton', 
                 background=[('active', '#818cf8')],
                 foreground=[('active', '#ffffff')])
        
        # Les entrées doivent avoir un fond clair et un texte foncé pour être lisibles
        style.configure('TEntry', 
                        fieldbackground='#f8fafc',  # Fond clair pour le champ
                        foreground='#1e293b',       # Texte foncé
                        insertcolor='#1e293b',      # Couleur du curseur
                        font=('Arial', 10))

        # Création du notebook (onglets)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=20, pady=20)

        # Créer les quatre onglets
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)
        self.tab4 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text="Création de compte")
        self.notebook.add(self.tab2, text="Confirmation investissement")
        self.notebook.add(self.tab3, text="Gains d'investissement")
        self.notebook.add(self.tab4, text="Déblocage licence")

        # Configurer chaque onglet
        self.setup_tab1()
        self.setup_tab2()
        self.setup_tab3()
        self.setup_tab4()

    def setup_tab1(self):
        # Formulaire 1: Création de compte
        form_frame = ttk.Frame(self.tab1)
        form_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Titre
        title_label = ttk.Label(form_frame, text="Création de compte d'investissement", font=("Arial", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10, sticky='w')

        # Champs de formulaire
        fields = [
            ("Email du destinataire:", "email1"),
            ("Nom:", "nom1"),
            ("Prénom:", "prenom1"),
            ("Téléphone:", "telephone1"),
            ("Pays:", "pays1"),
            ("Adresse:", "adresse1"),
            ("Adresse de portefeuille:", "portefeuille")
        ]

        for i, (label_text, attr_name) in enumerate(fields):
            ttk.Label(form_frame, text=label_text).grid(row=i+1, column=0, pady=5, padx=5, sticky='w')
            entry = ttk.Entry(form_frame, width=50)
            entry.grid(row=i+1, column=1, pady=5, padx=5, sticky='w')
            setattr(self, attr_name, entry)

        # Bouton d'envoi
        send_button = ttk.Button(form_frame, text="Envoyer l'email", command=self.send_email1)
        send_button.grid(row=len(fields)+1, column=0, columnspan=2, pady=20)

    def setup_tab2(self):
        # Formulaire 2: Confirmation investissement
        form_frame = ttk.Frame(self.tab2)
        form_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Titre
        title_label = ttk.Label(form_frame, text="Confirmation de compte d'investissement", font=("Arial", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10, sticky='w')

        # Champs de formulaire
        fields = [
            ("Email du destinataire:", "email2"),
            ("Nom:", "nom2"),
            ("Prénom:", "prenom2"),
            ("Téléphone:", "telephone2"),
            ("Pays:", "pays2"),
            ("Adresse:", "adresse2"),
            ("Capital investi (€):", "capital")
        ]

        for i, (label_text, attr_name) in enumerate(fields):
            ttk.Label(form_frame, text=label_text).grid(row=i+1, column=0, pady=5, padx=5, sticky='w')
            entry = ttk.Entry(form_frame, width=50)
            entry.grid(row=i+1, column=1, pady=5, padx=5, sticky='w')
            setattr(self, attr_name, entry)

        # Bouton d'envoi
        send_button = ttk.Button(form_frame, text="Envoyer l'email", command=self.send_email2)
        send_button.grid(row=len(fields)+1, column=0, columnspan=2, pady=20)

    def setup_tab3(self):
        # Formulaire 3: Gains d'investissement
        form_frame = ttk.Frame(self.tab3)
        form_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Titre
        title_label = ttk.Label(form_frame, text="Notification de gains d'investissement", font=("Arial", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10, sticky='w')

        # Champs de formulaire
        fields = [
            ("Email du destinataire:", "email3"),
            ("Nom:", "nom3"),
            ("Prénom:", "prenom3"),
            ("Téléphone:", "telephone3"),
            ("Pays:", "pays3"),
            ("Adresse:", "adresse3"),
            ("Capital investi (€):", "capital3"),
            ("Gains réalisés (€):", "gains")
        ]

        for i, (label_text, attr_name) in enumerate(fields):
            ttk.Label(form_frame, text=label_text).grid(row=i+1, column=0, pady=5, padx=5, sticky='w')
            entry = ttk.Entry(form_frame, width=50)
            entry.grid(row=i+1, column=1, pady=5, padx=5, sticky='w')
            setattr(self, attr_name, entry)

        # Bouton d'envoi
        send_button = ttk.Button(form_frame, text="Envoyer l'email", command=self.send_email3)
        send_button.grid(row=len(fields)+1, column=0, columnspan=2, pady=20)

    def setup_tab4(self):
        # Formulaire 4: Déblocage de licence
        form_frame = ttk.Frame(self.tab4)
        form_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Titre
        title_label = ttk.Label(form_frame, text="Déblocage de licence d'investissement", font=("Arial", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10, sticky='w')

        # Champs de formulaire
        fields = [
            ("Email du destinataire:", "email4"),
            ("Nom:", "nom4"),
            ("Prénom:", "prenom4"),
            ("Lien de paiement:", "lien_paiement")
        ]

        for i, (label_text, attr_name) in enumerate(fields):
            ttk.Label(form_frame, text=label_text).grid(row=i+1, column=0, pady=5, padx=5, sticky='w')
            entry = ttk.Entry(form_frame, width=50)
            entry.grid(row=i+1, column=1, pady=5, padx=5, sticky='w')
            setattr(self, attr_name, entry)

        # Bouton d'envoi
        send_button = ttk.Button(form_frame, text="Envoyer l'email", command=self.send_email4)
        send_button.grid(row=len(fields)+1, column=0, columnspan=2, pady=20)

    def validate_email(self, email):
        """Valide le format de l'adresse email"""
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email)

    def validate_form(self, email_field, required_fields):
        """Valide les champs du formulaire"""
        email = getattr(self, email_field).get().strip()
        if not email or not self.validate_email(email):
            messagebox.showerror("Erreur", "Veuillez entrer une adresse email valide.")
            return False

        for field in required_fields:
            if not getattr(self, field).get().strip():
                messagebox.showerror("Erreur", f"Tous les champs sont obligatoires.")
                return False
        return True

    def read_template(self, template_name):
        """Lit le contenu d'un fichier template HTML"""
        path = self.template_paths.get(template_name)
        if not os.path.exists(path):
            messagebox.showerror("Erreur", f"Le fichier template {path} est introuvable.")
            return None
        
        try:
            with open(path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de lire le template: {str(e)}")
            return None

    def send_email(self, to_email, subject, html_content):
        """Envoie un email avec le contenu HTML fourni"""
        message = MIMEMultipart('alternative')
        
        # Configuration des en-têtes d'email
        message['From'] = formataddr(('Simplex Trading', self.email))
        message['To'] = to_email
        message['Subject'] = Header(subject, 'utf-8')
        message['Date'] = datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z')
        message['Message-ID'] = f"<{datetime.now().strftime('%Y%m%d%H%M%S')}@{self.smtp_server}>"
        
        # Ajouter des en-têtes pour améliorer la délivrabilité
        message['X-Priority'] = '1'
        message['X-MSMail-Priority'] = 'High'
        message['Importance'] = 'high'
        message['X-Content-Type-Options'] = 'nosniff'
        message['X-Frame-Options'] = 'SAMEORIGIN'
        message['X-XSS-Protection'] = '1; mode=block'
        message['List-Unsubscribe'] = f'<mailto:{self.email}?subject=unsubscribe>'
        message['Precedence'] = 'bulk'
        message['X-Auto-Response-Suppress'] = 'OOF, AutoReply'

        # Ajouter une version texte simple
        text_content = "Cet email nécessite un client compatible HTML pour être correctement affiché."
        text_part = MIMEText(text_content, 'plain', 'utf-8')
        message.attach(text_part)

        # Ajouter la version HTML
        html_part = MIMEText(html_content, 'html', 'utf-8')
        message.attach(html_part)

        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email, self.password)
            server.send_message(message)
            server.quit()
            return True
        except Exception as e:
            messagebox.showerror("Erreur d'envoi", f"Impossible d'envoyer l'email: {str(e)}")
            return False

    def format_currency(self, value):
        """Formate un montant en euros avec séparateur de milliers"""
        try:
            value = float(value.replace(",", "."))
            return f"{value:,.2f}".replace(",", " ").replace(".", ",")
        except ValueError:
            messagebox.showerror("Erreur", "La valeur monétaire doit être un nombre valide.")
            return None

    def send_email1(self):
        """Envoie l'email de création de compte"""
        if not self.validate_form("email1", ["nom1", "prenom1", "telephone1", "pays1", "adresse1", "portefeuille"]):
            return

        # Récupérer les données du formulaire et nettoyer/échapper les caractères spéciaux
        to_email = self.email1.get().strip()
        nom = self.nom1.get().strip()
        prenom = self.prenom1.get().strip()
        telephone = self.telephone1.get().strip()
        pays = self.pays1.get().strip()
        adresse = self.adresse1.get().strip()
        portefeuille = self.portefeuille.get().strip()

        # Récupérer le template
        html_template = self.read_template("mail1")
        if not html_template:
            return

        # Formater le template avec les données
        try:
            html_content = html_template % (prenom, nom, prenom, to_email, telephone, pays, adresse, portefeuille)
            
            # Envoyer l'email
            if self.send_email(to_email, "Création de votre compte d'investissement", html_content):
                messagebox.showinfo("Succès", "L'email de création de compte a été envoyé avec succès!")
                # Réinitialiser le formulaire
                for field in ["email1", "nom1", "prenom1", "telephone1", "pays1", "adresse1", "portefeuille"]:
                    getattr(self, field).delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Erreur de formatage", f"Erreur lors du formatage du template: {str(e)}")

    def send_email2(self):
        """Envoie l'email de confirmation d'investissement"""
        if not self.validate_form("email2", ["nom2", "prenom2", "telephone2", "capital"]):
            return

        # Récupérer les données du formulaire
        to_email = self.email2.get().strip()
        nom = self.nom2.get().strip()
        prenom = self.prenom2.get().strip()
        telephone = self.telephone2.get().strip()
        capital = self.capital.get().strip()
        
        # Formater le capital
        formatted_capital = self.format_currency(capital)
        if not formatted_capital:
            return

        # Récupérer le template
        html_template = self.read_template("mail2")
        if not html_template:
            return

        # Formater le template avec les données
        try:
            html_content = html_template % (prenom, nom, prenom, to_email, telephone, formatted_capital)
            
            # Envoyer l'email
            if self.send_email(to_email, "Félicitations pour la création de votre compte d'investissement", html_content):
                messagebox.showinfo("Succès", "L'email de confirmation d'investissement a été envoyé avec succès!")
                # Réinitialiser le formulaire
                for field in ["email2", "nom2", "prenom2", "telephone2", "pays2", "adresse2", "capital"]:
                    getattr(self, field).delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Erreur de formatage", f"Erreur lors du formatage du template: {str(e)}")

    def send_email3(self):
        """Envoie l'email de notification de gains"""
        if not self.validate_form("email3", ["nom3", "prenom3", "telephone3", "capital3", "gains"]):
            return

        # Récupérer les données du formulaire
        to_email = self.email3.get().strip()
        nom = self.nom3.get().strip()
        prenom = self.prenom3.get().strip()
        telephone = self.telephone3.get().strip()
        capital = self.capital3.get().strip()
        gains = self.gains.get().strip()
        
        # Formater le capital et les gains
        formatted_capital = self.format_currency(capital)
        formatted_gains = self.format_currency(gains)
        if not formatted_capital or not formatted_gains:
            return

        # Récupérer le template
        html_template = self.read_template("mail3")
        if not html_template:
            return

        # Formater le template avec les données
        try:
            html_content = html_template % (prenom, nom, prenom, to_email, telephone, formatted_capital, formatted_gains)
            
            # Envoyer l'email
            if self.send_email(to_email, "Félicitations pour vos gains d'investissement !", html_content):
                messagebox.showinfo("Succès", "L'email de notification de gains a été envoyé avec succès!")
                # Réinitialiser le formulaire
                for field in ["email3", "nom3", "prenom3", "telephone3", "pays3", "adresse3", "capital3", "gains"]:
                    getattr(self, field).delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Erreur de formatage", f"Erreur lors du formatage du template: {str(e)}")

    def send_email4(self):
        """Envoie l'email de déblocage de licence"""
        if not self.validate_form("email4", ["nom4", "prenom4", "lien_paiement"]):
            return

        # Récupérer les données du formulaire
        to_email = self.email4.get().strip()
        nom = self.nom4.get().strip()
        prenom = self.prenom4.get().strip()
        lien_paiement = self.lien_paiement.get().strip()

        # Récupérer le template
        html_template = self.read_template("mail4")
        if not html_template:
            return

        # Formater le template avec les données
        try:
            html_content = html_template % (prenom, nom, lien_paiement)
            
            # Envoyer l'email
            if self.send_email(to_email, "Déblocage de votre licence d'investissement", html_content):
                messagebox.showinfo("Succès", "L'email de déblocage de licence a été envoyé avec succès!")
                # Réinitialiser le formulaire
                for field in ["email4", "nom4", "prenom4", "lien_paiement"]:
                    getattr(self, field).delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Erreur de formatage", f"Erreur lors du formatage du template: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = EmailApp(root)
    root.mainloop() 