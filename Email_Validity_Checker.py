
# Function to check whether an email is valid or not
def email_cek():
    # Ask user to input email
    email = input("Masukkan Email: ")
    
    # Check if email contains only one '@'
    if email.count('@') != 1:
        return print("Format Email Salah (tidak ada '@' atau '@' lebih dari 1)")

    # Split username and after '@' of an email into 2 variables based on '@'
    username, after_at = email.split('@')

    # Check whether the first character of the username is alphanumeric or not
    if not username[0].isalnum():
        return print("Format Email Salah (Huruf pertama Username harus huruf atau angka)")

    # Check whether the username contains only alphanumerics, or the characters '.', and '_'
    for char in username:
        if not (char.isalnum() or char in '._'):
            return print("Format Email Salah (Username tidak bisa mengandung karakter spesial, hanya boleh mengandung huruf, angka, titik, dan underscore)")

    # Check that the after_at variable contains a maximum of 2 '.' and a minimum of 1 '.'.Because Domains Extension can sometimes contain 2 dots or 1 dot (.com or .co.id)
    if after_at.count('.') > 2 or after_at.count('.') == 0:
        return print("Format Email Salah (setelah @ harus mengandung '.' dan hanya boleh mengandung maksimal 2 titik)")

    # Separate the hosting name and domain extension from the after_at variable based on First Dot (gmail (.) com / yahoo (.) co.id)
    hosting, extension = after_at.split('.', 1)

    # Check that the hosting name is alphanumeric
    if not hosting.isalnum():
        return print("Format Email Salah (Hosting harus huruf atau angka)")
    
    # if after splitting, the extension variable does not have '.' again (com) then run the following code
    if extension.count('.') == 0:
        # Check whether the extension domain is alphanumeric
        for char in extension:
            if not (char.isalpha()):
                return print("Format Email Salah (Ekstensi hanya boleh mengandung huruf)")
            
        # Check that the length of the extension is no more than 5 characters   
        if len(extension) > 5:
            return print("Format Email Salah (Ekstensi tidak boleh lebih dari 5 karakter)")

    # if after splitting, the extension variable has 1 '.' again (co.id) then run the following code
    elif extension.count('.') == 1:
        # Separate the domain extension into 2 variables, extension1 and extension2 if it contains 1 more dot (.)
        extension1, extension2 = extension.split('.')
        
        # Check if extension 1 is alphanumeric
        for char in extension1:
            if not (char.isalpha()):
                return print("Format Email Salah (Ekstensi 1 hanya boleh mengandung huruf)")
            
        # Check that the length of the extension is no more than 5 characters    
        if len(extension1) > 5:
            return print("Format Email Salah (Ekstensi 1 tidak boleh lebih dari 5 karakter)")
        
        # Check if extension 2 is alphanumeric
        for char in extension2:
            if not (char.isalpha()):
                return print("Format Email Salah (Ekstensi 2 hanya boleh mengandung huruf)")
            
        # Check that the length of the extension is no more than 5 characters   
        if len(extension2) > 5:
            return print("Format Email Salah (Ekstensi 2 tidak boleh lebih dari 5 karakter)")

    # If all conditions are met, the email is valid
    return print("Email Anda valid")

# Call the function
email_cek()