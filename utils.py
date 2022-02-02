def func_name():
    """
    obtengo el nombre de la funcion actual
    """
    import traceback
    return traceback.extract_stack(None, 2)[0][2]


def obtener_usuario(update):
    msg = update.message
    user_dic = {
        'id': msg.from_user.id,
        'first_name': msg.from_user.first_name,
        'is_bot': msg.from_user.is_bot,
        'last_name': msg.from_user.last_name,
        'username': msg.from_user.username,
    }
    return user_dic


def usuario_log(usuario):
    print(f"@{usuario['username']} presionó /start. --> ID:({usuario['id']}). "
          f"Nombre y Apellido: {usuario['first_name']}, {usuario['last_name']}")
