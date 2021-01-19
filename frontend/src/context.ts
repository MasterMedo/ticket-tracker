import { createContext } from "react";

interface AuthContextModel {
    isLoggedIn: boolean;
    token: string | undefined;
    login(username: string, password: string): void;
    logout(): void;
}

export const AuthContext = createContext<AuthContextModel>({
    isLoggedIn: false,
    token: '',
    login: (username, password) => {},
    logout: () => {}
});
