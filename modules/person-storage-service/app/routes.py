def register_routes(api, app, root="api"):
    from app.udaconnect import register_routes as attach_udaconnect_persons

    attach_udaconnect_persons(api, app)
