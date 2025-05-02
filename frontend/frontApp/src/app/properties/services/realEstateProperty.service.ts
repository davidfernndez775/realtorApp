import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { RealEstateProperty } from '../interfaces/realEstateProperty';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class RealEstatePropertyService {
  private baseUrl: string = 'http://127.0.0.1:8000/app/real-estate/list/';
  constructor(private http: HttpClient) {}

  getPropertyList(filters?: any): Observable<RealEstateProperty[]> {
    let params = new HttpParams();
    if (filters) {
      Object.keys(filters).forEach((key) => {
        if (filters[key]) {
          params = params.set(key, filters[key]);
        }
      });
    }

    return this.http.get<RealEstateProperty[]>(this.baseUrl, { params });
  }
}
