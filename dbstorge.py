#! /usr/bin/env python

import sqlite3
import time

series_columns = ['sid', 'title', 'link', 'cover', 'orgicover', 'timestamp', 'tag', 'fetch'];
series_table = 'series';

def openConnect(dbfile):
    return sqlite3.connect(dbfile)

def getSeriesByLink(conn, linkValue):
    cols = series_columns
    table = series_table
    sql = "select {columns} from {table} where {link}=?".format(columns=', '.join(cols), link=cols[2], table=table)
    # print "sql=",sql, 'link=', linkValue;
    cursor = conn.execute(sql, [linkValue])
    series = []
    for row in cursor:
        # print row
        item = {};
        for index, value in enumerate(cols):
            # print "{key} = {value}".format(key=value, value=row[index])
            item[value] = row[index]
        series.append(item);
    return series;

def saveSeries(conn, title, link, cover, orgicover='', timestamp=time.time(), tag='', fetch=0):
    cols = series_columns
    table = series_table
    sql = "insert into {table}({columns}) values (?, ?, ?, ?, ?, ?, ?)".format(table=table, columns=', '.join(cols[1:]))
    args = [title, link, cover, orgicover, timestamp, tag, fetch]
    # print 'sql=', sql, 'args=',args
    conn.execute(sql, args)
    conn.commit()

def saveSeriesOrgicover(conn, link, orgicover):
    cols = series_columns
    table = series_table
    sql = "update {table} set {orgicover}=? where {link}=?".format(table=table, orgicover=cols[4], link=cols[2])
    args = [orgicover, link]
    print 'sql=', sql, 'args=',args
    conn.execute(sql, args)
    conn.commit()
