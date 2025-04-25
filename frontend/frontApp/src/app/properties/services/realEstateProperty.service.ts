import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { RealEstatePropertyList } from '../interfaces/realEstateProperty';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class RealEstatePropertyService {
  private baseUrl: string = 'http://127.0.0.1:8000/app/real-estate';
  constructor(private http: HttpClient) {}

  getPropertyList(): Observable<RealEstatePropertyList[]> {
    return this.http.get<RealEstatePropertyList[]>(`${this.baseUrl}/list`);
  }
}
