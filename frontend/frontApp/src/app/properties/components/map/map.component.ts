import {
  AfterViewInit,
  ChangeDetectionStrategy,
  Component,
  ElementRef,
  ViewChild,
  Inject,
  PLATFORM_ID,
  OnDestroy,
} from '@angular/core';

import { isPlatformBrowser } from '@angular/common';
import { Map } from 'maplibre-gl';
import { environment } from '../../../../environments/environment';

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

      // 🔹 Forzar redibujado después de un breve delay
      setTimeout(() => {
        this.map?.resize();
      }, 500);
    }
  }

  ngOnDestroy() {
    this.map?.remove();
  }
}
