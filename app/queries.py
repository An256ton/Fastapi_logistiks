from .database import make_query

async def get_forwarder_by_id(id):
    q=f"select * FROM Forwarder where ForwarderID={id}"
    result= await make_query(q)
    return result
