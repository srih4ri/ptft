#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       pyter.py
#       
#       Copyright 2010 srihari <neo@trinity>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

def listdiff(a,b):
	c=[]
	for ax in a:
		if ax not in b:
			c.append(ax)
	
	return c

def main():
	import twitter
	api=twitter.Api('username','password')
	print 'Created twitter object'
	print 'Fetching followers ... '
	followers_users=api.GetFollowers()
	print 'Fetching friends ... '
	friends_users=api.GetFriends()
	followers_list=["@"+twitter_user._screen_name+"("+twitter_user.name+")" for twitter_user in followers_users]
	print "Opening file for writing followers list"
	f=open("followers.txt","a");
	f.writelines('\n')
	f.writelines(followers_list)
	f.close()
	print "followers.txt closed"
	friends_list=["@"+twitter_user._screen_name+"("+twitter_user.name+")"  for twitter_user in friends_users]
	print "Opening file to write friends list"
	f=open("friends.txt","a");
	f.writelines('\n')
	f.writelines(friends_list)
	f.close()
	print "friends file closed"
	print "The following are your followers that are not following you"
	non_belivers=listdiff(friends_list,followers_list) 
	for a in non_belivers:
		print a 
	
	print 'Calculating unfollowers'
	f=open("followers.txt","r")
	lines=f.readlines()
	lines.reverse()
	unfollowers=listdiff(lines[1].split('@'),lines[0].split('@'))
	print 'These are not following you anymore :'
	print unfollowers
	f.close()
	
	print 'Calculating new followers'
	f=open("followers.txt","r")
	lines=f.readlines()
	lines.reverse()
	newfollowers=listdiff(lines[0].split('@'),lines[1].split('@'))
	print 'These are your new followers:'
	print newfollowers
	f.close()
	return 0
	
if __name__ == '__main__':
	main()
	
	

	 
