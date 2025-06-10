import { HttpClient, HttpParams } from '@angular/common/http';
import { computed, inject, Injectable, signal } from '@angular/core';
import { environment } from '../../../environments/environment';
import { User } from '../interfaces/user.interface';
import { AuthStatus } from '../interfaces/authStatus.enum';
import { map, Observable, of, tap } from 'rxjs';
import { LoginResponse } from '../interfaces/response.interface';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  // *URL address
  private readonly baseUrl: string = environment.baseUrl;
  private registerUrl: string = `${this.baseUrl}/auth/register/`;
  private loginUrl: string = `${this.baseUrl}/auth/login/`;
  private http = inject(HttpClient);

  // *User status
  private _currentUser = signal<User | null>(null);
  private _authStatus = signal<AuthStatus>(AuthStatus.checking);

  // *public
  public currentUser = computed(() => this._currentUser());
  public authStatus = computed(() => this._authStatus());
  constructor() {}

  // *functions
  register() {}

  login(email: string, password: string): Observable<boolean> {
    const body = { email, password };
    return this.http.post<LoginResponse>(this.loginUrl, body).pipe(
      tap(({ user, token }) => {
        this._currentUser.set(user);
        this._authStatus.set(AuthStatus.authenticated);
        localStorage.setItem('token', token);
        console.log({ user, token });
      }),
      map(() => true)
    );
  }
}
