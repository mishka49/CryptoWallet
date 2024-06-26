import {deleteToken} from "../services/auth_token";

export default function LogoutPage({redirect}) {
    deleteToken()

    return redirect
}