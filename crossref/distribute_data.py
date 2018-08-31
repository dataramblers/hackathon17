import lzma


def separate_data():
    with lzma.open('/home/swissbib/Dokumente/open_access/crossref_dump/crossrefworks.json.xz',
                   'rt', encoding='utf-8') as f:
        count = 0
        lines = list()
        line = f.readline()
        print(line)
        while line:
            lines.append(line)
            count += 1
            line = f.readline()
            if count % 100000 == 0:
                print("Read 100000 Lines.")
                with lzma.open('/home/swissbib/Dokumente/open_access/crossref_dump/split_data/crossref_' +
                               str(count) + '.json.xz', 'wt', encoding='utf-8') as xs:
                    for l in lines:
                        xs.write(l)
                lines.clear()


separate_data()
