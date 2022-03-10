use sym - resource - order - manager

db.getCollection('resourceOrders').aggregate([
    { "$match": { "organizationCode": { "$in": ["IZZIMX", "AXTELLEGO", "IZZIMXHFC"] }, "status": { "$in": ["FAILED"] }, "createdDate": { "$lt": new Date(), "$gte": new Date(new Date().setDate(new Date().getDate() - 1)) } } },
    { "$group": { "_id": { "organizationCode": '$organizationCode', "errorMessage": "$errorMessage", "resourceType": "$resourceType", }, "count": { "$sum": 1 } } },
    { "$project": { "organizationCode": '$_id.organizationCode', "errorMessage": "$_id.errorMessage", "resourceType": "$_id.resourceType", "total": "$count" } },
    { "$sort": { "_id.organizationCode": 1, "total": -1 } }
]).forEach(function(x) {
    print(x._id.organizationCode + ',' + x._id.errorMessage.replace(',', '') + ',' + x._id.resourceType + ',' + x.total)
})