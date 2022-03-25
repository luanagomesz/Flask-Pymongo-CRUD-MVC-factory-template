from datetime import datetime
from typing import Union
from flask import jsonify
from ..exceptions.posts_exc import PostNotFoundError
import pymongo
from pymongo import ReturnDocument

client = pymongo.MongoClient("mongodb://localhost:27017/")


class post:
    db = client['kenzie']

    def __init__(self, **kwargs) -> None:
        self.title = kwargs['title']
        self.author = kwargs['author']
        self.tags = kwargs['tags']
        self.content = kwargs['content']
        self.id = self.register_id()
    


    def register_id(self):
        cursor = list(self.db.posts.find())
        print(cursor)
        newId = 1
        for key in cursor:
            if '_id'in key:
                if key["_id"] == newId:
                    newId = newId + 1
        return newId
    
    def create_post(self):
        date = datetime.utcnow()
        post = {"title": self.title, "author": self.author, "tags": self.tags, "content": self.content, "_id": self.id, "created_at":date , "update_at": date}
        self.db.posts.insert_one(post)
        return list(self.db.posts.find({'_id': self.id}))

    @classmethod
    def get_post_by_id(cls,id):
        return list(cls.db.posts.find({"_id": id}))
        
    @classmethod
    def get_all_posts(cls):
        return jsonify(list(cls.db.posts.find()))

    @classmethod
    def update_post(cls, data, id):
        post = list(cls.db.posts.find({"_id": id}))
        date = datetime.utcnow()
        data["update_at"] = date
        update_post = cls.db.posts.find_one_and_update({"_id": id}, {"$set": data}, upsert=False, return_document=ReturnDocument.AFTER)

        if not update_post:
            raise PostNotFoundError

        if post == list(update_post):
            return "invalid keys"
        
        return update_post
    
    @classmethod   
    def delete_post(cls, id):
        post = cls.db.posts.find({'_id': id})
        arr = list(post)
        if arr == list([]):
           
            raise PostNotFoundError
            
        cls.db.posts.delete_one({'_id': id})
        return arr

        
