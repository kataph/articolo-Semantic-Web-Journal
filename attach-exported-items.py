with open("progetto-ricerca.bib","a") as f1:
    with open("Exported items.bib","r") as f2:
        s = f2.read()
        f1.write(s)
        length = len(s)
        print(f"Copied {length} character")
    
