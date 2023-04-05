import os

headersData = {
    "AdblockVPNGuide.md": [":name_badge:", "140", "# Adblocking / Privacy", "Adblocking, Privacy, VPN's, Proxies, Antivirus"]
}

def getHeaderForPage(pageFilename):
    data = headersData[pageFilename]
    header = "---\n" + "icon: " + data[0] + "\n" + "order: " + data[1] + "\n" + "---\n" + data[2] + "\n"  + data[3] + "\n\n"
    return header

def apply_to_all_md_files_in_current_dir():
    files = os.listdir('.')
    for file in files:
        if file in headersData:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                if not content.startswith('---'):
                    print("adding header to " + file)
                    with open(file, 'w', encoding='utf-8') as f2:
                        header = getHeaderForPage(file)
                        f2.write(header+content)

apply_to_all_md_files_in_current_dir()