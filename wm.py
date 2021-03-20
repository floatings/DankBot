import urllib.request, json, re

def parseweb(url, i=1):
    resArr = []
    page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    infile=urllib.request.urlopen(page).read().decode('utf8')
    data = json.loads(infile)
    for item in data['data']['menu_items']:
        try:
            product = item['name'] + " - $" + str(item['price']['original_price'])
        except:
            continue
        print(product)
        res = str(i) + ". " + product
        resArr.append(res)
        i = i+1
    return (data['meta']['total_menu_items'], i, resArr)

dict = [["vape","cart"],["wax","concentrate","dab"],["tree","flower","bud","weed"],["edibles","food"]]

def scrape(url, category, storetype="dispensaries"):
    char = ''
    category = category.lower().strip()
    if (category=='v') or (category=='1')or any(word in category for word in dict[0]):
        category = "vape-pens"
        char = '(V) '
    elif (category=='c') or (category=='2') or (category=='w') or any(word in category for word in dict[1]):
        category = "concentrates"
        char = '(C) '
    elif (category=='f') or (category=='3') or (category=='t') or any(word in category for word in dict[2]):
        category = "flower"
        char = '(F) '
    elif (category=='e') or (category=='4') or any(word in category for word in dict[3]):
        category = "edibles"
        char = '(E) '
    else:
        print("Category not found")

    disp = url
    plainurl = "https://api-g.weedmaps.com/discovery/v1/listings/dispensaries/storename/menu_items?include%5B%5D=facets.categories&page_size=150&page=1&filter%5Bany_categories%5D%5B%5D=thiscategory&sort_by=min_price&sort_order=asc"
    url = plainurl.replace("storename", url)
    url = url.replace("thiscategory", category)
    if(storetype=="deliveries"):
        url = url.replace("dispensaries", "deliveries")
    print(url)
    pgsize = "150"

    print("\n" + disp.replace("-"," ").title() + " - " + category.replace("-"," ").title())
    print(url)
    sc = parseweb(url)

    pg = 1
    if(sc [0]> int(pgsize)):
        pg = pg + 1
        url = url.split("page=")
        nextpage = url[0] + "page=" + str(pg) + url[1][1:]
        parseweb(nextpage,sc[1])
    return (sc[2],category, disp, char)

