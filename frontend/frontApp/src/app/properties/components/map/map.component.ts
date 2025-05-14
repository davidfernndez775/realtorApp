import {
  AfterViewInit,
  ChangeDetectionStrategy,
  Component,
  ElementRef,
  ViewChild,
  Inject,
  PLATFORM_ID,
  OnDestroy,
  Input,
} from '@angular/core';

import { isPlatformBrowser } from '@angular/common';
import { Color, Map, Marker } from 'maplibre-gl';
import { environment } from '../../../../environments/environment';
import { RealEstateProperty } from '../../interfaces/realEstateProperty';
import { map } from 'rxjs';

@Component({
  selector: 'app-map',
  standalone: true,
  imports: [],
  templateUrl: './map.component.html',
  styleUrl: './map.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class MapComponent implements AfterViewInit, OnDestroy {
  map: Map | undefined;
  @ViewChild('map', { static: false }) mapContainer?: ElementRef<HTMLElement>;
  @Input() properties: RealEstateProperty[] | null = null;

  public markers: Marker[] = [];

  constructor(@Inject(PLATFORM_ID) private platformId: any) {}

  ngAfterViewInit(): void {
    if (isPlatformBrowser(this.platformId)) {
      const initialState = { lng: -80.34599, lat: 25.7578, zoom: 10 };

      if (!this.mapContainer) throw 'HTML Element not found';

      this.map = new Map({
        container: this.mapContainer.nativeElement,
        style: `https://api.maptiler.com/maps/streets-v2/style.json?key=${environment.maplibre_key}`,
        center: [initialState.lng, initialState.lat],
        zoom: initialState.zoom,
      });

      this.map.on('load', () => {
        // Asegurarse de que el mapa está cargado antes de añadir marcadores
        if (this.properties) {
          this.properties.forEach((property) => this.createMarker(property));
        }
      });

      // 🔹 Forzar redibujado después de un breve delay
      setTimeout(() => {
        this.map?.resize();
      }, 500);
    }
  }

  createMarker(property: RealEstateProperty) {
    let color: string = 'red';
    // check the colors of markers
    if (property.price_decrease === true) {
      color = 'yellow';
    }
    if (property.new === true) {
      color = 'blue';
    }
    // call the marker
    this.addMarker(property.lon, property.lat, color);
    console.log('createmarker');
  }

  addMarker(lng: number, lat: number, color: string = 'red') {
    // check if there is a map object
    if (!this.map || !this.properties) return;

    const marker = new Marker({
      color: color,
    })
      .setLngLat([lng, lat])
      .addTo(this.map);

    console.log('addmarker');
  }

  ngOnDestroy() {
    this.map?.remove();
  }
}
