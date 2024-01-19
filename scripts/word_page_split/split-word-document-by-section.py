import aspose.words as aw

# load Word document
doc = aw.Document("document.docx")

for i in range(0, doc.sections.count) :
            
    # clone the section to split
    section = doc.sections[i].clone()

    # create an instance of Document class for new doucment
    newDoc = aw.Document()
    
    # clear the default sections
    newDoc.sections.clear()

    # inster section into new document
    newSection = newDoc.import_node(section, True).as_section()
    newDoc.sections.add(newSection)

    # Save section as a separate document
    newDoc.save(f"split_by_sections_{i}.docx")