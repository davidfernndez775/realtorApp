import { User } from './user.interface';

export interface RegisterResponse {
  user: User;
}

export interface LoginResponse {
  user: User;
  token: string;
}
